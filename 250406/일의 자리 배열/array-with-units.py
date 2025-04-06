first, second = map(int, input().split())
arr = [first, second]

for i in range(3, 11):
    arr.append(arr[-1] + arr[-2])

arr2 = []

for elem in arr:
    if elem < 10:
        arr2.append(elem)
    elif elem >= 10:
        arr2.append(elem % 10)
    elif elem >= 100:
        arr2.append(elem % 100)

# for elem in arr2:
#     print(elem, end=' ')

for i in range(len(arr2)):
    print(arr2[i], end=' ')