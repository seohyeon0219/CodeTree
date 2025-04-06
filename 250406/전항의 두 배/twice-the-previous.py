first, second = map(int, input().split())
arr = [first, second]

for i in range(2, 10, 1):
    arr.append(arr[i-1] + 2 * arr[i-2])

for elem in arr:
    print(elem, end=' ')
    