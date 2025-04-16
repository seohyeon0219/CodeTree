n = int(input())
arr = list(map(int, input().split()))
cnt, idx = 0, 0

for i in range(n):
    if arr[i] == 2:
        cnt += 1
        if cnt == 3:
            idx = i

print(idx + 1)
