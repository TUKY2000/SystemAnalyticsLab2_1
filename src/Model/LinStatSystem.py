import numpy as np
import scipy.linalg as sp
import math
import sys

class Functional:
    '''
    class describes square funcеional of management quality \n
    I = 0.5 * integral{tr(x(t))*S(t)*x(t) + tr(u(t))*Q(t)*u(t)} + 0.5 * tr(x(t1))*pi*x(t1)
    '''
    def __init__(self, matrixS : list, matrixQ : list, matrixPi : list):
        self.mS = np.matrix(matrixS)
        self.mQ = np.matrix(matrixQ)
        self.mPi = np.matrix(matrixPi)



class LinStatSystem:
    '''
    Linear stacionary system can be described by math equations \n
    x'(t) = A(t)*x(t) + B(t)*u(t), \n
    y(t) = C(t)*x(t), x(t_0) = x_0
    '''

    def __init__(self, matrixA : list, matrixB : list, matrixC : list, startState : list):
        self.mA = np.matrix(matrixA)
        self.mB = np.matrix(matrixB)
        self.mC = np.matrix(matrixC)
        self.x0 = startState

    def __dxdt(self, x, u):
        return np.dot(self.mA, x) + np.dot(self.mB, u)

    def reaction(self, state):
        return np.dot(self.mC, state)


class LSSManagement(list):
    '''
    Array of managment to manage linear stacionary system
    '''
    def manage(self, system : LinStatSystem, time, quantPeriod):
        if not self.__check(time, quantPeriod):
            raise ValueError('length of management should be equal to (time / quantPeriod) value')
        mPhi = self.__getPhi(system, quantPeriod)
        mG = self.__getG(mPhi, system)
        states = self.__findStates(system, mPhi, mG)
        return np.squeeze(states), np.squeeze(self.__findSysReaction(states, system))

    def __check(self, time, T0):
        return time == int(T0 * len(self))

    def __getPhi(self, system : LinStatSystem, qPeriod):
        mI = np.eye(system.mA.shape[0])    # create unit matrix
        result = mI
        for i in range(5):
            result += (system.mA * qPeriod) ** (i + 1) /  math.factorial(i + 1)
        return result

    def __getG(self, mPhi, system):
        return ((mPhi - np.eye(system.mA.shape[0])) * np.linalg.inv(system.mA)) * system.mB

    def __nextState(self, vX ,mPhi, mG, currtime):
        ''' find next vector x_(k+1) '''
        return np.dot(mPhi, vX) + np.dot(mG, self[currtime])

    def __findStates(self, system : LinStatSystem, mPhi, mG):
        ''' returns array of all vectors 'x' for current vL '''
        result = [system.x0]
        for k in range(0, len(self)):
            result.append(self.__nextState(result[-1], mPhi, mG, k))
        return result

    def __findSysReaction(self, arrayX, system : LinStatSystem):
        result = []
        for x in arrayX:
            result.append(system.reaction(x))
        return result


class LSSManagementOpt(LSSManagement):
    '''
    Generates optimal management for linear stacionar system and its quality functional
    '''
    def __init__(self, system : LinStatSystem, func : Functional, states : list):
        self = self.__generate(system.mA, system.mB, func.mQ, func.mS, states)

    def __generate(self, mA, mB, mQ, mS, states):
        return  np.dot(np.dot(mQ.I, mB.T),
                np.dot(sp.solve_continuous_are(mA, mB, mS, mQ), states))