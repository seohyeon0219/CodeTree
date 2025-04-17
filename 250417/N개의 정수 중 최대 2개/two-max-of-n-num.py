n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

for i in range(2):
    print(arr[i], end=' ')