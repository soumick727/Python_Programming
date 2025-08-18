n = 3
for i in range(n+1):
    for j in range(i):
        print("*", end="")
    print()
    
##pyramid
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*", end="")
    print()