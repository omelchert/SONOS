# FILE: main_EX_Fig1b.py 
#
# USAGE EXAMPLE FOR SONOS:
#   main code implementing problem setup consisting of a single absorbing layer
#
# AUTHOR: O. Melchert
# DATE:   19.05.2016
import sys; sys.path.append('../src/')
from SONOS import *

def main():
        # INI COMPUTATIONAL DOMAIN --------------------------------------------
        zMax   = 0.15
        Nz     = 150
        rhoMax = 0.30
        Nrho   = 3000
        Nphi   = 1
        # INI BEAM PARAMETERS -------------------------------------------------
        a      = float(sys.argv[2]) # 0.1 
        R      = float(sys.argv[3]) # 4.0 
        # INI MATERIAL PARAMETERS ---------------------------------------------
        c0     = 150000.
        z10, z11, ma1  = 0.00, 0.10, 20.0
        # INI MEASUREMENT PARAMETERS ------------------------------------------
        xD     = 0.
        zD     = -float(sys.argv[1])
        dr     = 0.001

        ## SET COMPUTATIONAL DOMAIN -------------------------------------------
        (z,dz)     = np.linspace(0 ,zMax,   Nz,   retstep=True, endpoint=False)
        (rho,drho) = np.linspace(0 ,rhoMax, Nrho, retstep=True, endpoint=False)
        (phi,dphi) = np.linspace(0 ,2*np.pi,Nphi, retstep=True, endpoint=False)

        ## SET ABSORBTION-PARAMETER DEPTH PROFILE -----------------------------
        mu_z = np.zeros(z.size) 
        ## SET TISSUE LAYERS --------------------------------------------------
        setLayer(mu_z,z10,z11,dz,ma1)

        ## COMPUTE OPTOACOUSTIC SIGNAL ----------------------------------------
        S_z      = axialAbsorptionProfile(mu_z,z,dz) 
        iProf    = lambda x,y: radialBeamProfile_topHat(x,y,a,R)
        p_zD_t   = OASignal((zD,xD),(z,dz,S_z),(rho,drho,phi,dphi,iProf),dr)

        print "# (t) \t (c tau) \t (p(zD,t))"
        for i in range(p_zD_t.size):
                print "%g \t %g \t %g"%(i*dz/c0,i*dz+zD, p_zD_t[i])

main()
# EOF: main_EX_Fig2a.py 
