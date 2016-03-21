1. INTRODUCTION

SONOS - a faSt pOisson iNtegral sOlver foR layered hOmogeneouS media

implements a stand-alone python module for the numerical simulation of
photoacoustic signals in non-scattering, layered media. Therein, the
calculation of the excess pressure is accomplished via the optoacoustic Poisson
integral, based on a representation of the volumetric energy density within the
source volume in cylindrical polar coordinates.

Two use-cases that illustrate the simulation of optoacoustic signals for 
layered media on and off the beam axis are detailed in the examples folder. 

So as to avoid unnecessary overhead, the implementation follows a procedural
programming style.


2. DEPENDENCIES

SONOS requires the functionality of NumPy, a fundamental package for scientific
computing (see www.numpy.org).


3. CONTENT

README.txt              -- this readme document
LICENSE.txt             -- BSD 3-Clause License file

src/
    SONOS.py            -- python module 

examples/
    main_EX_Fig2a.py    -- main python code implementig simulation setup 
    main_EX_Fig2b.py    -- main python code implementig simulation setup 
    main_EX_Fig3.py     -- main python code implementig simulation setup 
    
    getData_EX2.sh      -- bash script
    getData_EX3.sh      -- bash script
    
    EX_Fig2/
       cyl_2Layer_high_low_zD0.04.dat   -- data file
       cyl_2Layer_high_low_zD4.0.dat    -- data file
       cyl_2Layer_low_high_zD0.04.dat   -- data file
       cyl_2Layer_low_high_zD4.0.dat    -- data file
       GP/
          SONOS_NF_FF.gpi       -- gnuplot file 
          FIGS/
             SONOS_NF_FF.eps    -- eps figure (draft)

    EX_Fig3/
       cyl_2Layer_low_high_zD0.2_xD0.00.dat     -- data file
       cyl_2Layer_low_high_zD0.2_xD0.10.dat     -- data file
       cyl_2Layer_low_high_zD0.2_xD0.20.dat     -- data file
       cyl_2Layer_low_high_zD1.0_xD0.00.dat     -- data file
       cyl_2Layer_low_high_zD1.0_xD0.10.dat     -- data file
       cyl_2Layer_low_high_zD1.0_xD0.20.dat     -- data file
       cyl_2Layer_low_high_zD5.0_xD0.00.dat     -- data file
       cyl_2Layer_low_high_zD5.0_xD0.10.dat     -- data file
       cyl_2Layer_low_high_zD5.0_xD0.20.dat     -- data file
       GP/
           SONOS_xDScan.gpi             -- gnuplot file
           FIGS/
              SONOS_xDScan_NF_FF.eps    -- eps figure (draft)


4. LICENSE

BSD 3-Clause License


5. ACKNOWLEDGEMENTS

O. Melchert acknowledges support from the VolkswagenStiftung within the
Nieders\"achsisches Vorab program in the framework of the project Hybrid
Numerical Optics. 
