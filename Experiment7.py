n=int(input("enter a number"))
for i in range(1,n):
    for j in range(1,n):
        if (i*i + j*j ) ==n and (i<j):
            print(i,j)
