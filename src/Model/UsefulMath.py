def RungeKutta4(func, x0, y0, steplen, x1):
    def f1(x, y):
        return func(x, y)

    def f2(x, y):
        return func(x + 0.5*steplen, y + 0.5*f1)

    def f3(x, y):
        return func(x + 0.5*steplen, y + 0.5*f2)

    def f4(x, y):
        return func(x + steplen, y + f3)

    def __next(x, y):
        return y + h * (f1(x,y) + 2*f2(x,y) + 2*f3(x,y) + f4(x,y)) / 6
    
    X = [x0]
    Y = [y0]
    stepcount = x1 / steplen
    for i in range(stepcount):
        X.append(X[i] + steplen)
        Y.append(__next(func, X[i], Y[i], steplen))
    return X, Y