arr = list(map(int, input().split()))
arr2, arr3 = [] , []
for elem in arr:
    if elem < 500:
        arr2.append(elem)
    else:
        arr3.append(elem)

print(max(arr2), min(arr3))