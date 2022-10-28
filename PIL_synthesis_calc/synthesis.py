"""
Created by Michael Hassett on 10/09/2022 at 3:51 pm
Basic PIL synthesis calculator
"""

import numpy as np

class Chemical:
    """Detail of a generic chemical.
    If both a mass and volume are provided, the mass value will be accepted and override the volume
    Additional details on the function

    :ivar molweight: Molecular weight in g/mol
    :ivar conc: Concentration in wt%
    :ivar pKa: pKa of the chemical
    :ivar density: Density in g/mL
    """

    def __init__(self,
                 name: str,
                 *,
                 molweight: np.single,
                 conc: np.single,
                 pKa: np.single,
                 mass: np.single = None,
                 density: np.single = None,
                 volume: np.single = None,
                 stoic: np.single = 1):
        self.name = name
        self.molweight = np.single(molweight)  # Molecular weight in g/mol
        # If wt% concentration is given in whole values, make a decimal for ease of calculation
        if conc is not None and conc > 1:
            self.conc = np.single(conc / 100)    # Concentration in wt%
        else:
            self.conc = np.single(conc)          # Concentration in wt%

        self.pKa = np.single(pKa)

        # Mass is prioritised, so if a mass is provided, the volume will be over
        if mass is not None:
            self.mass = np.single(mass)
            if volume is not None:
                self.volume = np.single(volume)
                self.density = np.single(self.mass/self.volume)
            else:
                self.density = np.single(density)
                self.volume = np.single(self.mass / self.density)
        elif volume is not None:
            self.volume = np.single(volume)
            if density is not None:
                self.density = np.single(density)
                self.mass = np.single(self.volume * self.density)
            else:
                print("Warning: Density is being approximated. Please provide a density or a")
                self.density = self.molweight / (
                        (self.acid.stoic * self.acid.molweight) / (self.acid.conc * self.acid.density) +
                        (self.base.stoic * self.base.molweight) / (self.base.conc * self.base.density))
                self.mass = (self.density * self.volume)
        else:
            raise ValueError("mass or volume must be assigned")
        self.mole = np.single(self.mass / self.molweight)
        self.stoic = np.short(stoic)

    def print_characterisation(self, sigfigs: np.single = 4):
        print(f'Name: {self.name}')
        print(f'Molecular Weight: {np.format_float_positional(self.molweight, precision=sigfigs)} g/mol')
        print(f'pKa: {np.format_float_positional(self.pKa, precision=sigfigs)}')
        print(f'Density: {np.format_float_positional(self.density, precision=sigfigs)} g/mL')
        print(f'Concentration: {np.format_float_positional(self.conc * 100, precision=sigfigs)} wt%')
        print(f'Mass: {np.format_float_positional(self.mass, precision=sigfigs)} g')
        print(f'Mole: {np.format_float_positional(self.mole, precision=sigfigs)} mol')
        print(f'Volume: {np.format_float_positional(self.volume, precision=sigfigs)} mL')
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
                 molweight: np.single,
                 conc: np.single,
                 pKa: np.single,
                 density: np.single = None,
                 stoic: np.short = 1):
        super().__init__(name=name,
                         molweight=molweight,
                         conc=conc,
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
        self.mole = np.single(self.stoic * mole)
        self.mass = np.single((self.mole * self.molweight) / self.conc)
        self.volume = np.single(self.mass / self.density)


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
                 stoic: np.short = 1):
        self.acid = acid
        self.base = base
        super().__init__(name=name,
                         molweight=(self.acid.molweight + self.base.molweight),
                         mass=mass,
                         volume=volume,
                         density=density,
                         conc=None,
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
                         molweight=45.08,
                         conc=0.66,
                         pKa=10.65,
                         density=0.81)
    nitric_acid = Reagent("Nitric Acid",
                          molweight=63.01,
                          conc=0.7,
                          pKa=-1.38,
                          density=1.42)

    EAN = PIL("EAN", base=ethylamine, acid=nitric_acid, mass=20)
    # EAN = PIL("EAN", ethylamine, nitric_acid, volume=20)

    ethylamine.print_characterisation()
    nitric_acid.print_characterisation()
    EAN.print_characterisation()