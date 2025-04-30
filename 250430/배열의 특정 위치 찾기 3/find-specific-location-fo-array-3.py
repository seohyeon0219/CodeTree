arr = list(map(int, input().split()))

if 0 in arr:
    i = arr.index(0)

sum = sum(arr[i-3:i])
print(sum)
