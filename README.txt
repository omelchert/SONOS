1. INTRODUCTION

SONOS - a faSt pOisson iNtegral sOlver foR layered hOmogeneouS media

implements a stand-alone python module for the numerical simulation of
photoacoustic signals in non-scattering, layered media. Therein, the
calculation of the excess pressure is accomplished via the optoacoustic Poisson
integral, based on a representation of the volumetric energy density within the
source volume in cylindrical polar coordinates.

Four use-cases that illustrate the simulation of optoacoustic signals for 
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
    main_EX_Fig5a_PI.py   -- main python code implementig simulation setup 
    main_EX_Fig5b_PII.py  -- main python code implementig simulation setup 
    main_EX_Fig5c_PIII.py -- main python code implementig simulation setup 
    main_EX_Fig6.py     -- main python code implementig simulation setup 
    
    getData_EX2.sh      -- bash script
    getData_EX3.sh      -- bash script
    getData_EX5.sh      -- bash script
    getData_EX6.sh      -- bash script
    
    EX_Fig2/
       cyl_2Layer_high_low_zD0.04.dat   -- data file
       cyl_2Layer_high_low_zD4.0.dat    -- data file
       cyl_2Layer_low_high_zD0.04.dat   -- data file
       cyl_2Layer_low_high_zD4.0.dat    -- data file
       GP/
          SONOS_NF_FF.gpi       -- gnuplot file 
          FIGS/
             SONOS_NF_FF.eps    -- eps figure (draft)
             SONOS_NF_FF.pdf    -- pdf figure (draft)

    EX_Fig3/
       cyl_2Layer_low_high_*.dat     -- data files
       GP/
           SONOS_xDScan.gpi             -- gnuplot file
           FIGS/
              SONOS_xDScan_NF_FF.eps    -- eps figure (draft)
              SONOS_xDScan_NF_FF.pdf    -- pdf figure (draft)

    EX_Fig5/
        T_PI.dat        -- data file
        T_PII.dat       -- data file
        T_PIII.dat      -- data file
        GP/
           TvsE_hig_low_v2.gpi  -- gnuplot file
           dummy.dat   -- data file
           FIGS/
                TvsE_pz_PI_PII_PIII.eps -- eps figure (draft)
                TvsE_pz_PI_PII_PIII.pdf -- pdf figure (draft)

    EX_Fig6/
        
        getMSE.sh               -- bash script
        MSE.dat                 -- data file
        cyl_PIII_zD*.dat        -- data files
        GP/
           PIII_p0.gpi          -- gnuplot file 
           dummy.dat            -- data file
           FIGS/
                TvsE_p0_predictor_MSE_PIII.eps -- eps figure (draft)
                TvsE_p0_predictor_MSE_PIII.pdf -- pdf figure (draft)


4. LICENSE

BSD 3-Clause License


5. ACKNOWLEDGEMENTS

O. Melchert acknowledges support from the VolkswagenStiftung within the
Nieders\"achsisches Vorab program in the framework of the project Hybrid
Numerical Optics. 

