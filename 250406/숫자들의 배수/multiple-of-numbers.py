n = int(input())
arr = []

for i in range(n, 100, n):
    print(i, end=' ')
    if i % 5 == 0:
        arr.append(i)
    if len(arr) == 2:
        break

