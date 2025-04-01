n = int(input())

for i in range(n):
    for j in range(0, 2*i+1, 1):
        print('*', end='')
    print()
