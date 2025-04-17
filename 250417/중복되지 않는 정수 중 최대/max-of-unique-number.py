n = int(input())
arr = list(map(int, input().split()))
arr2 = []

for i in range(n):
    if arr.count(arr[i]) == 2:
        continue
    else:
        arr2.append(arr[i])

if len(arr2) > 0:
    print(max(arr2))
else:
    print(-1)