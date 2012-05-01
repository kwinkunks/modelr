'''
Created on May 1, 2012

@author: sean
'''

from . import zoep_calc
class RockProperties(object):
    '''
    Class to store rock properties.
    
    :param vp: pressure wave coef
    :param vs: shear wave coef
    :param rho: TODO
    
    '''
    
    def __init__(self, vp, rho, vs=None):
        self.vp = vp
        if vs is None:
            self.vs = vp / 2.0
        else:
            self.vs = vs
        self.rho = rho
        
def zoeppritz(Rp0, Rp1, theta1):
    
    return zoep_calc.zoeppritz(Rp0.vp, Rp0.vs, Rp0.rho,
                               Rp1.vp, Rp1.vs, Rp1.rho,
                               theta1)    
