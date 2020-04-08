def func(x):
    return x*x -24
def deri(x):
    return 2*x

def newton_method(x):
    while True:
        xResult = x - (func(x) / deri(x))
        # print("the result is",xResult)
        if (func(xResult)==0 or abs(x-xResult<0.0004)):
            print(xResult)
            break
        elif(func(xResult)!=0):
            x=xResult
        else:
            print("invalid")
            break
val=int(input("Enter a value "))
newton_method(val)
