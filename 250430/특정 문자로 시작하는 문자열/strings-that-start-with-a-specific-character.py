n = int(input())
arr = [input() for _ in range(n)]
m = input()
cnt = 0
sum = 0

for i in range(n):
    if arr[i][0] == m:
        cnt += 1
        sum += len(arr[i])
print(cnt)
print(f'{cnt} {sum/cnt:.2f}')