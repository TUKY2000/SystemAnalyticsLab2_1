import numpy as np
import scipy as sp

class Functional:
    '''
    class describes square funcеional of management quality \n
    I = 0.5 * integral{tr(x(t))*S(t)*x(t) + tr(u(t))*Q(t)*u(t)} + 0.5 * tr(x(t1))*pi*x(t1)
    '''
    def __init__(self, matrixS : list, matrixQ : list, matrixPi : list,):
        self.mS = np.matrix(matrixS)
        self.mQ = np.matrix(matrixQ)
        self.mPi = np.matrix(matrixPi)



class LinStatSystem:
    '''
    Linear stacionary system can be described by math equations \n
    x'(t) = A(t)*x(t) + B(t)*u(t), \n
    y(t) = C(t)*x(t), x(t_0) = x_0
    '''

    def __init__(self, matrixA : list, matrixB : list, matrixC : list, status : list):
        self.mA = np.matrix(A)
        self.mB = np.matrix(B)
        self.mC = np.matrix(C)
        self.x0 = status


class LSSManagement(list):
    '''
    Array of managment to manage linear stacionary system
    '''
    def manage(self, system : LinStatSystem, time):
        quantPeriod = int(time / len(self))
        mPhi = self.__getPhi(system, quantPeriod)
        mG = self.__getG(mPhi, system)
        states = self.__findStates(system, mPhi, mG)
        return states, self.__findSysReaction(states)

    def __getPhi(self, system : LinStatSystem, qPeriod):
        mI = np.eye(3)    # create unit matrix
        result = mI
        for i in range(5):
            result += (system.mA * qPeriod) ** (i + 1) /  math.factorial(i + 1)
        return result

    def __getG(self, mPhi, system):
        return ((mPhi - np.eye(3)) * np.linalg.inv(system.mA)) * system.mB

    def __nextState(self, vX ,mPhi, mG, currtime):
        ''' find next vector x_k+1 '''
        return mPhi * vX + mG * self[currtime]

    def __findStates(self, system : LinStatSystem, mPhi, mG):
        ''' returns array of all vectors 'x' for current vL '''
        result = []
        x = system.x0.copy()
        for k in range(0, len(self)):
            result.append(x)
            x = self.__nextX(x, mPhi, mG, k)                  
        return result

    def __findSysReaction(self, arrayX):
        result = []
        for x in arrayX:
            result.append(self.__getY(x))
        return result


class LSSManagementOpt(LSSManagement):
    '''
    Generates optimal management for linear stacionar system and its quality functional
    '''
    def __init__(self, system : LinStatSystem, func : Functional):
        super(LSSManagementOpt, self).__init__(self.__generate(system.mA, system.mB, func.mQ, func.mS))

    def __generate(self, mA, mB, mQ, mS):
        return np.dot(np.dot(np.linalg.inv(mQ), mB.T), sp.linalg.solve_continuous_are(mA, mB, mS, mQ))