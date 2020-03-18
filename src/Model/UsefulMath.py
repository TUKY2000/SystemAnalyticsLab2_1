def ModRungeKutta4(func, x0, y0, x1, steplen):
    '''
    solve differencial equation
    '''
    def __next(x, y):
        k1 = func(x, y)
        k2 = func(x, y + 0.5*k1)
        k3 = func(x + 1, y + 0.5*k2)
        k4 = func(x + 1, y + k3)
        return y + steplen * (k1 + 2*k2 + 2*k3 + k4) / 6
    
    X = [x0]
    Y = [y0]
    stepcount = int((x1 - x0) / steplen - 1)
    for i in range(stepcount):
        X.append(X[i] + steplen)
        Y.append(__next(i, Y[i]))
    return X, Y