arr = list(map(int, input().split()))
arr2 = []

for elem in arr:
    if elem != 0:
        arr2.append(elem)
    else:
        break

for i in range(len(arr2)):
    if arr2[i] % 2 == 1:
        arr2[i] += 3
    else:
        arr2[i] //= 2

print(*arr2)