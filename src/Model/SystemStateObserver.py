import LinStatSystem as lss
import numpy as np
import UsefulMath as usm

class FullOrderObserver:
    '''
    Generates estimation of the system states when rank y equal rank x
    '''

    def __init__(self, system : lss.LinStatSystem):
        self.system = system

    def estimate(self, managment : list, sysreaction : list, mK : np.matrix, time, qper):
        def __dxdt(t, x):
            return np.dot(self.system.mA, x) +\
                np.dot(self.system.mB, managment[t]) +\
                np.dot(mK, (sysreaction[t] - np.dot(self.system.mC, x)))
        
        return usm.ModRungeKutta4(__dxdt, 0, self.system.x0, time, steplen = qper)

    

class LowOrderObserver:
    '''
    Generates estimation of the system states when rank y is lower rank x
    '''

    def __init__(self, system : lss.LinStatSystem):
        self.system = system

    def estimate(self, managment, sysraction, matrixD, matrixK, time, qper):
        # 1) check input
        
        def __calcG(mD, mK):
            # 0) define dimensions
            _Adim = (self.system.mA.shape[0], self.system.mA.shape[1])
            _N = _Adim[0]
            _NminusK = _Adim[0] - mD.shape[0]
            _Udim = (_Adim[0] * _NminusK, _Adim[0] * _NminusK)

            # 1) build matrix of linear combinations G*A => U1
            U1 = []
            
            for row in range(_NminusK):
                for col in range(_N):
                    linComb = [0] * (row*_N)
                    for k in range((mD.shape)[1]):
                        linComb.append(self.system.mA[k, col])
                    while linComb.count < _Udim:
                        linComb.append(0)
                    U1.append(linComb)

            # 2) build matrix of linear combinations D*G => U2
            U2 = []

            for row in range(_NminusK):
                for col in range(_N):
                    linComb = []
                    for k in range((mD.shape)[1]):
                        linComb.append(self.system.mA[k, col])
                        for _ in range(_N - 1):
                            linComb.append(0)
                    U2.append(linComb)
            
            # 3) U = U1 - U2
            U = np.matrix(np.matrix(U1) - np.matrix(U2))

            # 4) create vector of matrix K*C elements => M
            vM = np.dot(mK, self.system.mC).flatten()

            # 5) solve U*x=M => x = U^(-1) * M
            vectG = np.dot(np.linalg.inv(U), vM)
            # 6) create G
            mG = vectG.reshape(_NminusK, _N)
            return mG

        def __calcH(mG):
            return np.dot(mG, self.system.mB)

        # 2) calc additional matrces
        mG = __calcG(matrixD, matrixK)
        mH = __calcH(mG)

        # 3) calculate additional system reaction estimation => vZ
        def __dzdt(t, z):
            return np.dot(matrixD, z) + np.dot(mH, managment) + np.dot(matrixK, sysraction)

        estimateZ = usm.ModRungeKutta4(__dzdt, self.system.x0, 0, time, steplen = qper)

        # 4) calculate estimation x
        estimateX = np.dot(np.linalg.inv(np.append(self.system.mC, mG)),
            np.append(sysraction, estimateZ))

        return estimateX