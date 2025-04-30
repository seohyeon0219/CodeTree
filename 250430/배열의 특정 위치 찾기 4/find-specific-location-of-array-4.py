arr = list(map(int, input().split()))

if 0 in arr:
    i = arr.index(0)
    arr = arr[:i]

sum, cnt = 0, 0

for elem in arr:
    if elem % 2 == 0:
        sum += elem
        cnt += 1

print(cnt, sum)