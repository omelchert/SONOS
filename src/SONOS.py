"""FILE: SONOS.py 

Module implementing functions for 

SONOS - a faSt pOisson iNtegral sOlver foR layered hOmogeneouS media

The calculation of the excess pressure via the optoacostic Poisson integral is
based on a representation of the volumetric energy density within the source
volume in cylindrical polar coordinates.

AUTHOR: O. Melchert
DATE:   11.03.2016
"""
import numpy as np

def setLayer(mu_z,z0,z1,dz,ma):
        """set tissue layer

        \param[in]  mu_z absorption coefficient profile 
        \param[in]  z0   start of new tissue layer 
        \param[in]  z1   end of new tissue layer 
        \param[in]  ma   absorption coefficient 
        """
        mu_z[int(z0/dz):int(z1/dz)] = ma


def axialAbsorptionProfile(mu_z,z,dz):
        """axial absorption profile

        \param[in]  mu_z absorption coefficient profile 
        \param[in]  z    z-axis
        \param[in]  dz   axial increment
        \param[out] aap  axial absorption profile 
        """
        return mu_z*np.exp(-np.cumsum(mu_z*dz))


def radialBeamProfile_flatTop(x,y,a):
        """Top hat beam profile

        \param[in]  x   x-position for profile computation
        \param[in]  y   y-position for profile computation
        \param[in]  a   radial extension of flat-top component 
        \param[in]  R   1/e-width of beam profile
        \param[out] isp radial irradiation source profile
        """
        if (x**2+y**2) <= a*a: 
                return 1.0
        else:
                return 0.0 


def radialBeamProfile_topHat(x,y,a,R):
        """Top hat beam profile

        \param[in]  x   x-position for profile computation
        \param[in]  y   y-position for profile computation
        \param[in]  a   radial extension of flat-top component 
        \param[in]  R   1/e-width of beam profile
        \param[out] isp radial irradiation source profile
        """
        if (x**2+y**2) <= a*a: 
                return 1.0
        else:
                return np.exp(-(np.sqrt(x**2+y**2)-a)**2/(a/R)**2)


def radialBeamProfile_Gaussian(x,y,a):
        """Gaussian beam profile

        \param[in]  x   x-position for profile computation
        \param[in]  y   y-position for profile computation
        \param[in]  a   1/e-width of beam profile
        \param[out] isp radial irradiation source profile
        """
        return np.exp(-(np.sqrt(x**2+y**2)/a)**2)


def OASignal((zD,xD),(z,dz,g),(rho,drho,phi,dphi,f),dr):
        """optoacoustic signal at detector position 
        
        fast solver for the optoacoustic Poisson integral based on a 
        representation of the volumetric energy density within the source 
        volume in cylindrical polar coordinates

        \param[in]  zD    z-coordinate of detector 
        \param[in]  xD    x-coordinate of detector 
        \param[in]  z     z-axis 
        \param[in]  dz    increment along z-axis 
        \param[in]  g     axial absorption profile 
        \param[in]  rho   radial axis 
        \param[in]  drho  radial increment 
        \param[in]  phi   discretized azimuthal angle
        \param[in]  dphi  azimuthal angle increment 
        \param[in]  f     radial irradiation source profile 
        \param[in]  dr    width of the transdrucer foil 
        \param[out] pt    optoacoustic signal at detector position 
        """
        # DECLARATION AND INITIALIZATION --------------------------------------
        z     = z - zD
        f_D   = lambda r,p: f(xD+r*np.cos(p),r*np.sin(p))
        F_D   = np.zeros(rho.size)
        dn    = max(int(dr/dz/2),2) 
        I     = np.zeros(int(np.sqrt(max(abs(z))**2 + max(rho)**2)/dz) + 1)
        pDt   = np.zeros(I.size)

        # INTEGRATION, PART I: ------------------------------------------------
        # yield contribution of irradiation source profile for energy 
        # absorption along planar circles of infinitesimal width 
        # Preconditioning step with time-complexity O(rho.size phi.size)
        for i,rho_i in enumerate(rho):
            for j,phi_j in enumerate(phi):
                F_D[i] += rho_i*f_D(rho_i,phi_j)*dphi

        # INTEGRATION, PART II: -----------------------------------------------
        # complete integration over energy density by integrating over the
        # axial absorption profile 
        # Pendding integrations can be carried out in time O(z.size rho.size)
        for i,z_i in enumerate(z):
            for j,rho_j in enumerate(rho):
                ct = np.sqrt(z_i**2+rho_j**2)
                # binning acording to radial distance to detector
                I[int(ct/dz)] += g[i]*F_D[j]*dz*drho/ct

        # NUMERICAL DERIVATIVE TO YIELD OA SIGNAL -----------------------------
        # average OA signal over the width of the transducer foil
        I = np.cumsum(I)
        for i in range(1+dn,I.size-1-dn):
            pDt[i] = ((I[i+dn+1]-I[i-dn+1]) - (I[i+dn-1]-I[i-dn-1]))/(4.0*dz*dn)

        return pDt


# EOF: SONOS.py 
