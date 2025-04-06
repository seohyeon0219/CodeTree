arr = list(map(int, input().split()))
arr2 = []

for elem in arr:
    if elem == 0:
        continue
    elif elem % 2 == 1:
        arr2.append(elem + 3)
    elif elem % 2 == 0:
        arr2.append(elem // 2)

for elem in arr2:
    print(elem, end=' ')