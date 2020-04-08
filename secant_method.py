from math import *
def func(x):
    return x*x*x-4*x+4
    # return x*x*x*x-x-10
    # return x*exp(x)-cos(x*180/(pi))

def secant_method(x0,x1):
    # while True:
    while True:
        x2 = x1 - (func(x1) *(x1 - x0)) / (func(x1) - func(x0))
        errConvergence=(x2-x1)/x1
        if func(x2)>0:
            x1=x2
        elif func(x2)==0:
            print(x2)
            print(errConvergence)
            break
        else:
            x0=x2

x0=float(input("enter a number"))
x1=float(input("enter another number"))
secant_method(x0,x1)
