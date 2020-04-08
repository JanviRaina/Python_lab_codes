# def func(x):
#     return x*x-2*x-8
# def bissection(x1,x2):
#     if func(x1)*func(x2)<0:
#         xResult=(x1+x2)/2
#         if(func(xResult)==0):
#             break
#         elif(func(xResult)>0):
#             bissection(x1,xResult)
#         else:
#             bissection(xResult,x2)
#     else:
#         print("invalid")
# bissection(1,6)
#

def func(x):
    return x*x-2*x-8
def bissection( x1, x2):
    while True:
        xResult = (x1 + x2) / 2
        if(func(x1)*func(x2)<0):
            # xResult=(x1+x2)/2
            if (func(xResult) > 0):
                x2=xResult
            elif (func(xResult) < 0):
                x1=xResult
            else:
                print(xResult)
                break
        else:
            print("invalid")
            break
a=int(input("Enter first value"))
b=int(input("Enter second value"))
bissection(a,b)
# bissection(-1,-6)
# bissection(-6,-1)
