arr = list(map(int, input().split()))

if 0 in arr:
    i = arr.index(0)
    arr = arr[:i]

print(f'{sum(arr)} {sum(arr)/len(arr):.1f}')