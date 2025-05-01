arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        arr2 = arr[:i]

# print(max(arr2), min(arr2))

max_val, min_val = arr[0], arr[0]

for i in range(len(arr2)):
    if arr2[i] > max_val:
        max_val = arr2[i]
    if arr2[i] < min_val:
        min_val = arr2[i]

print(max_val, min_val)

