def func(x):
    return x*x -5*x +4
def deri(x):
    return 2*x -5
def newton_method(x):
    while True:
        xResult = x - (func(x) / deri(x))
        if (func(xResult)==0 and abs(x-xResult<0.0004)):
            print(xResult)
            # print(count)
            break
        elif(func(xResult)!=0):
            x=xResult
        else:
            print("invalid")
            break
val=int(input("Enter a value "))
newton_method(val)
