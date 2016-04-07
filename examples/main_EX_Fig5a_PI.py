# FILE: main_EX_Fig2a.py 
#
# USAGE EXAMPLE FOR SONOS:
#   main code implementing problem setup consisting of 2 absorbing layers 
#
# AUTHOR: O. Melchert
# DATE:   21.03.2016
import sys; sys.path.append('../src/')
from SONOS import *

def main():
        # INI COMPUTATIONAL DOMAIN --------------------------------------------
        zMax   = 0.30
        Nz     = 300
        rhoMax = 0.30
        Nrho   = 3000
        Nphi   = 3
        # INI BEAM PARAMETERS -------------------------------------------------
        a      = 0.054 
        R      = 1.5
        # INI MATERIAL PARAMETERS ---------------------------------------------
        c0     = 150000.
        z10, z11, ma1  = 0.00, 0.095, 11.
        # INI MEASUREMENT PARAMETERS ------------------------------------------
        xD     = 0.
        zD     = -0.3
        dr     = 0.005

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

        p0   = lambda i: 0 if (i<0 or i>=Nz) else S_z[i]
        n1   = np.sum([p0(i) for i in range(p_zD_t.size)])
        p0FF = lambda i: np.trapz(p_zD_t[:i],dx=dz/c0)
        n2   = np.sum([p0FF(i) for i in range(p_zD_t.size)])
        mse  = 0.
        print "# (t) \t (c tau) \t (p0) \t (pzD) \t (p0FF)"
        for i in range(p_zD_t.size):
                mse += (p0(i+int(zD/dz))/n1 - p0FF(i)/n2 )**2
                print "%g \t %g \t %g \t %g \t %g"%(i*dz/c0,i*dz+zD,p0(i+int(zD/dz))/n1,p_zD_t[i]/dr,p0FF(i)/n2)

        # MEAN SQUARED ERROR OF THE PREDICTOR p0FF
        print "# MSE ", zD, mse/p_zD_t.size

main()
# EOF: main_EX_Fig2a.py 
