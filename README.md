
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mph759/PIL_project">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PIL project</h3>

  <p align="center">
    This project is an attempt to make a cohesive database and corresponding calculators for PIL synthesis, as well as other common PIL processes, pulling known data for precursors and PILs alike
    <br />
    <a href="https://github.com/mph759/PIL_project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mph759/PIL_project">View Demo</a>
    ·
    <a href="https://github.com/mph759/PIL_project/issues">Report Bug</a>
    ·
    <a href="https://github.com/mph759/PIL_project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

<p>This project seeks to simplify the synthesis and processing of PILs, such that simple,
repeated calculations and searching of basic literature values can be done in relative ease, and en masse.
For further details on  features, see the <a href="#roadmap">Roadmap</a> below</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.com]][Python-url]
* [![PostgreSQL][PostgreSQL.com]][PostgreSQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

<!--This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
-->
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* numpy
  ```sh
  pip install numpy
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/mph759/PIL_project.git
   ```
3. Run the `synthesis.py` script
   ```sh
   python PIL_synthesis_calc/synthesis.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Currently, the scripts are only capable of taking manually input chemical values and synthesising PILs according to those values.

<!--_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Calculating the required amounts of precursers necessary to synthesise a target mass or volume of PIL
- [ ] Database of precursor data to pull automatically from, removing need to manually input precursor data
- [ ] Identification of precursors given requested PIL 
- [ ] Calculations for serial dilutions to mol% and wt% targets

See the [open issues](https://github.com/mph759/PIL_project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

1. Michael Hassett - s3717891@student.rmit.edu.au - [LinkedIn](https://linkedin.com/in/mph759)
2. Stuart Brown - [LinkedIn](https://linkedin.com/in/stuartbrown12)

Project Link: [https://github.com/mph759/PIL_project](https://github.com/mph759/PIL_project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
This work is being undertaken as a side project of related PhD work at RMIT University.
This work is done in association with our supervisor A/Prof. Tamar Greaves

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mph759/PIL_project.svg?style=for-the-badge
[contributors-url]: https://github.com/mph759/PIL_project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mph759/PIL_project.svg?style=for-the-badge
[forks-url]: https://github.com/mph759/PIL_project/network/members
[stars-shield]: https://img.shields.io/github/stars/mph759/PIL_project.svg?style=for-the-badge
[stars-url]: https://github.com/mph759/PIL_project/stargazers
[issues-shield]: https://img.shields.io/github/issues/mph759/PIL_project.svg?style=for-the-badge
[issues-url]: https://github.com/mph759/PIL_project/issues
[license-shield]: https://img.shields.io/github/license/mph759/PIL_project.svg?style=for-the-badge
[license-url]: https://github.com/mph759/PIL_project/blob/master/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=twitter&colorB=555
[twitter-url-MPH]: https://twitter.com/mph_759
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-MPH]: https://linkedin.com/in/mph759
[linkedin-url-SB]: https://linkedin.com/in/stuartbrown12
[product-screenshot]: images/screenshot.png
[Python.com]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[PostgreSQL.com]: https://img.shields.io/badge/PostgreSQL-2f6087?style=for-the-badge&logo=PostgreSQL&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
