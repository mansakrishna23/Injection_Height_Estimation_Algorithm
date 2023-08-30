# Injection_Height_Estimation_Algorithm
A injection height estimation algorithm using Doppler Radar data. 

The following repository contains the python scripts for an injection height estimation algorithm using WSR-88D dual polarization data. Also included in the repository are Jupyter Notebooks as references for plotting figures and data analysis. 

### Citation for this code:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8184701.svg)](https://doi.org/10.5281/zenodo.8184701) (older release)

Krishna, M., Saide, P. E., Ye, X., Turney, F., Hair, J. W., Fenn, M., & Shingler, T. Evaluation of Plume Injection Heights Estimated from Operational Weather Radar Observations \[Manuscript in Preparation\]

## References
### Datasets 
- NOAA Next Generation Radar (NEXRAD) Level II WSR-88D data from Radar KOTX
  - NOAA National Weather Service (NWS) Radar Operations Center (1991): NOAA Next Generation Radar (NEXRAD) Level 2 Base Data. NOAA National Centers for Environmental Information. doi:10.7289/V5W9574V [11/12/2020].
- Airborne lidar DIAL-HSRL from DC-8 aircraft, during the FIREX-AQ field campaign.
  - NASA/LARC/SD/ASDC. (2020). FIREX-AQ DC-8 In-Situ Aerosol Data [Data set]. NASA Langley Atmospheric Science Data Center DAAC. Retrieved from https://doi.org/10.5067/ASDC/FIREXAQ_Aerosol_AircraftInSitu_DC8_Data_1

### Software
The code and scripts in this repository are in written in Python, `Python version 3.9.7`, available under the license https://python.org/. The following Python libraries were used in the injection height estimation algorithm, for creating figures and tables, and for data analysis. 
  - Python specific packages that were imported for the code include `os.py` and `warnings.py`
- The Python ARM Radar Toolkit `Py-ART version 1.11.6` was used for interpreting the radar data, and creating objects used within the injection height estimation algorithm, https://arm-doe.github.io/pyart/
  - Helmus, J., & Collis, S. (2016). The Python ARM Radar Toolkit (Py-ART), a Library for Working with Weather Radar Data in the Python Programming Language. Journal of Open Research Software, 4(1), e25. https://doi.org/10.5334/jors.119
- `NumPy version 1.21.2`, available under the license https://numpy.org/
  - Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).
- `Matplotlib version 3.4.3`, available under the license https://matplotlib.org/ 
  - J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.
- `SciPy version 1.2.1`, available under the license https://scipy.org/
  - Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E.A. Quintero, Charles R Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.
- `Pandas version 1.2.5`, available under the license https://pandas.pydata.org/
  - The pandas development team. (2021, June). pandas-dev/pandas: Pandas 1.2.5. Retrieved from https://doi.org/10.5281/zenodo.5013202
  - Data structures for statistical computing in python, McKinney, Proceedings of the 9th Python in Science Conference, Volume 445, 2010.
  
