import LinStatSystem as lss
import numpy as np
import UsefulMath as usm

class FullOrderObserver:
    '''
    Generates estimation of the system states when rank y equal rank x
    '''

    def __init__(self, system : lss.LinStatSystem):
        self.system = system

    def estimate(self, managment : list, sysreaction : list, mK : np.matrix, time):
        return usm.RungeKutta4(self.__dxdt, self.system.x0, 0, steplen = 100, time)

    def __dxdt(x, t):
        return np.dot(self.system.mA, x) 
        + np.dot(self.system.mB, self.u) 
        + np.dot(self.mK,(self.y - np.dot(self.system.mC, x)))

class LowOrderObserver:
    '''
    Generates estimation of the system states when rank y is lower rank x
    '''

    def __init__(self, system : lss.LinStatSystem):
        self.system = system

    def estimate(self, managment : list, sysraction : list, )