arr = list(map(int, input().split()))

if 0 in arr:
    i = arr.index(0)
    arr = arr[:i]

for elem in arr[::-1]:
    print(elem, end=' ')