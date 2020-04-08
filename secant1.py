def func(x):
    return x*x-2*x
def secant_method( x1, x2):
    if (func(x1) * func(x2) < 0):
        while True:
            xResult = x2 - (func(x2) *(x2 - x1)) / (func(x2) - func(x1))
            errConvergence=abs((x2-x1)/x1)
            # print (xResult)
                # xResult=(x1+x2)/2
                if (func(xResult) > 0):
                    x2=xResult
                elif (func(xResult) < 0):
                    x1=xResult
                else:
                    print(xResult)
                    print(errConvergence)
                    break
secant_method(1,2)
