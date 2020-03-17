def RungeKutta4(func, x0, y0, x1, steplen):
    '''
    solve differencial equation
    '''
    def f1(x, y):
        return func(x, y)

    def f2(x, y):
        return func(x + 0.5*steplen, y + 0.5*f1)

    def f3(x, y):
        return func(x + 0.5*steplen, y + 0.5*f2)

    def f4(x, y):
        return func(x + steplen, y + f3)

    def __next(x, y):
        return y + steplen * (f1(x,y) + 2*f2(x,y) + 2*f3(x,y) + f4(x,y)) / 6
    
    X = [x0]
    Y = [y0]
    stepcount = int((x1 - x0) / steplen)
    for i in range(stepcount):
        X.append(X[i] + steplen)
        Y.append(__next(X[i], Y[i]))
    return X, Y