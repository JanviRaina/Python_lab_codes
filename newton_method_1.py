def func(x):
    return 2*x*x*x -9.5*x +7.5
def deri(x):
    return 6*x*x-9.5

def newton_method(x):
    while True:
        xResult = x - (func(x) / deri(x))
        if (func(xResult)==0 and abs(x-xResult<0.0004)):
            print(xResult)
            break
        elif(func(xResult)!=0):
            x=xResult
        else:
            print("invalid")
            break
val=int(input("Enter a value "))
newton_method(val)
