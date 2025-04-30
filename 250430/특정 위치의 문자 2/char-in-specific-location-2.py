arr = list(input().split())

for elem in arr[1:len(arr):3]:
    print(elem, end=' ')