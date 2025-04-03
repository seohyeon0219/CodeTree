n = int(input()) # 5

for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

for i in range(n-1): # 4, i=0,1,2,3
    for j in range(n+i-3): #3,4,5,6
        print("*", end=" ")
    print()