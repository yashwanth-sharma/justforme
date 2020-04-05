# identitymatrix
n=int(input("enter the number of rows needed for the identity matrix:"))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
