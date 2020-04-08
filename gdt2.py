def f1(x,y,z):
    return 5*x+3*y+7*z-4
def f2(x,y,z):
    return 3*x+26*y+2*z-9
def f3(x,y,z):
    return 7*x+2*y+11*z-5
def gauss(y0,z0):
    count=1
    x1=1/5*(4-3*y0-7*z0)
    y1=1/26*(9-2*z0-3*x1)
    z1=1/11*(5-7*x1-2*y1)
    if(f1(x1,y1,z1)==0):
        print(x1)
        print(y1)
        print(z1)
        print("The no. of iterations are",count)
    else:
        count += 1
        y0=y1
        z0=z1
        gauss(y0,z0)

y0=0
z0=0
gauss(y0,z0)