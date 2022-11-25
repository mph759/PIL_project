"""
Created by Michael Hassett on 10/09/2022 at 3:51 pm
Basic PIL synthesis calculator
"""

import numpy as np
from astropy import units as u

wtpct = u.def_unit('wt%')
molpct = u.def_unit('mol%')


class Chemical:
    """Detail of a generic chemical.
    If both a mass and volume are provided, the mass value will be accepted and override the volume
    Additional details on the function

    :ivar mol_weight: Molecular weight in g/mol
    :ivar conc: Concentration in wt%
    :ivar pKa: pKa of the chemical
    :ivar density: Density in g/mL
    """

    def __init__(self,
                 name: str,
                 *,
                 mol_weight: np.single,
                 concentration: np.single,
                 pKa: np.single,
                 mass: np.single = None,
                 density: np.single = 1,
                 volume: np.single = None,
                 stoic: np.single = 1):

        self.name = name
        self.mol_weight = u.Quantity(np.single(mol_weight), u.g / u.mol)  # Molecular weight in g/mol
        self.pKa = np.single(pKa)
        self.stoic = np.short(stoic)

        # Mass is prioritised, so if a mass is provided, the volume will be over
        if mass is not None:
            self.mass = u.Quantity(np.single(mass), u.g)
            if volume is not None:
                self.volume = u.Quantity(np.single(volume), u.ml)
                self.density = np.single(self.mass / self.volume)
            else:
                self.density = u.Quantity(np.single(density), u.g / u.ml)
                self.volume = u.Quantity(np.single(self.mass / self.density), u.ml)
        elif volume is not None:
            self.volume = u.Quantity(np.single(volume), u.ml)
            self.density = u.Quantity(np.single(density), u.g / u.ml)
            if density == 1:
                print(
                    f"Warning: Density of {self.name} is being approximated as {self.density.value} {self.density.unit}\n")
            self.mass = (self.density * self.volume)
        else:
            raise ValueError("mass or volume must be assigned")
        self.mole = u.Quantity(np.single(self.mass / self.mol_weight), u.mol)

        # If wt% concentration is given in whole values, make a decimal for ease of calculation
        if concentration is not None:
            self.conc = u.Quantity(concentration, wtpct)
        else:
            self.conc = u.Quantity(np.single(None), wtpct)

    def get_mol_wieght(self):
        return self.mol_weight

    def get_conc(self):
        return self.conc

    def get_pKa(self):
        return self.pKa

    def get_mass(self):
        return self.mass

    def get_density(self):
        return density

    def get_volume(self):
        return self.volume

    def get_stoic(self):
        return self.stoic

    def wtpct_to_molpct(self, *, internal: bool = False):
        if self.conc.unit == wtpct:
            self.conc = u.Quantity(18 / (18 + self.get_mol_weight().value * ((1 / self.get_conc().value) - 1)), molpct)
        elif not internal:
            print(f"Concentration of {self.name} is already in {self.conc.unit}, needs to be {wtpct}")

    def molpct_to_wtpct(self, *, internal: bool = False):
        if self.conc.unit == molpct:
            self.conc = u.Quantity(self.get_mol_weight().value / (self.get_mol_weight().value - 18 * (1 - 1 / self.get_conc().value)),
                                   wtpct)
        elif not internal:
            print(f"Concentration of {self.name} is already in {self.conc.unit}, needs to be {molpct}")

    def print_characterisation(self, sigfigs: np.single = 4):
        print(f'Name: {self.name}')
        print(
            f'Molecular Weight: {np.format_float_positional(self.mol_weight.value, precision=sigfigs)} {self.mol_weight.unit}')
        print(f'pKa: {np.format_float_positional(self.pKa, precision=sigfigs)}')
        print(f'Density: {np.format_float_positional(self.density.value, precision=sigfigs)} {self.density.unit}')
        print(f'Concentration: {np.format_float_positional(self.conc.value * 100, precision=sigfigs)} {self.conc.unit}')
        print(f'Mass: {np.format_float_positional(self.mass.value, precision=sigfigs)} {self.mass.unit}')
        print(f'Mole: {np.format_float_positional(self.mole.value, precision=sigfigs)} {self.mole.unit}')
        print(f'Volume: {np.format_float_positional(self.volume.value, precision=sigfigs)} {self.volume.unit}')
        print()


class Reagent(Chemical):
    """Detail of a reagent

    Additional details on the function

    :ivar molweight: Molecular weight in g/mol
    :ivar conc: Concentration in wt%
    :ivar density: Density in g/mL
    :ivar stoic: Stoichiometric ratio, or how many hydrogens it is willing to donate/take

    :ivar mass: Mass of the reagent in g
    :ivar volume: Volume of the reagent in mL
    :ivar mole: Mole of the reagent in mol
    """

    def __init__(self,
                 name: str,
                 *,
                 mol_weight: np.single,
                 concentration: np.single,
                 pKa: np.single,
                 density: np.single = None,
                 stoic: np.short = 1):
        super().__init__(name=name,
                         mol_weight=mol_weight,
                         concentration=concentration,
                         pKa=pKa,
                         mass=1,
                         density=density,
                         stoic=stoic)
        self.mass = None
        self.volume = None

    def __edit_mole__(self, mole):
        """
        Edit mole, mass and volume

        Determine the mole, mass and volume required of the reagents to obtain the target mole value
        """
        self.mole = u.Quantity(np.single(self.stoic * mole), u.mol)
        if self.conc.unit == wtpct:
            self.mass = (self.mole * self.mol_weight) / self.conc.value
        else:
            self.molpct_to_wtpct(internal=True)
            self.mass = (self.mole * self.mol_weight) / self.conc.value
            self.wtpct_to_molpct(internal=True)
        self.volume = self.mass / self.density


class PIL(Chemical):
    """Detail of a PIL

    Additional details on the function

    :ivar acid: Acid/Hydrogen donor reagent in the PIL synthesis
    :type acid: Reagent
    :ivar base: Base/Hydrogen acceptor reagent in the PIL synthesis
    :type base: Reagent

    :ivar mass: Required yield mass of PIL. Default=None
    :ivar volume: Required yield volume of PIL. Default=None
    :ivar density: Density in g/mL. Default=None
    """

    def __init__(self,
                 name: str,
                 base: Reagent,
                 acid: Reagent,
                 *,
                 mass: np.single = None,
                 volume: np.single = None,
                 density: np.single = None,
                 concentration: np.single = None,
                 stoic: np.short = 1):
        self.acid = acid
        self.base = base
        super().__init__(name=name,
                         mol_weight=(self.acid.mol_weight + self.base.mol_weight),
                         mass=mass,
                         volume=volume,
                         density=density,
                         concentration=concentration,
                         pKa=(self.base.pKa - self.acid.pKa),
                         stoic=stoic)
        self.synthesise()

    def synthesise(self):
        """
        Synthesis

        Determine the mole, mass and volume required of the reagents to obtain the target mole value
        """
        self.acid.__edit_mole__(self.mole / self.stoic)
        self.base.__edit_mole__(self.mole / self.stoic)


if __name__ == '__main__':
    ethylamine = Reagent("Ethylamine",
                         mol_weight=45.08,
                         concentration=0.66,
                         pKa=10.65,
                         density=0.81)
    nitric_acid = Reagent("Nitric Acid",
                          mol_weight=63.01,
                          concentration=0.7,
                          pKa=-1.38,
                          density=1.42)

    EAN = PIL("EAN", base=ethylamine, acid=nitric_acid, mass=20)
    # EAN = PIL("EAN", ethylamine, nitric_acid, volume=20)

    ethylamine.print_characterisation()
    nitric_acid.print_characterisation()
    EAN.print_characterisation()
