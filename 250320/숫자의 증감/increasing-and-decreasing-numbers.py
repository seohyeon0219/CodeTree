arr = input().split()
c = arr[0]
n = int(arr[1])
i = 1

if c == 'A':
    for i in range(i, n+1, 1):
        print(i, end=' ')
elif c == 'D':
    for i in range(n, i-1, -1):
        print(i, end=' ')
    