n = int(input())
arr = [1, n]

while arr[-1] < 100:
    arr.append(arr[-2] + arr[-1])

print(*arr)