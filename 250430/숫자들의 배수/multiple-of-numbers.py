n = int(input())
arr = []
cnt = 0
i = 1

while cnt < 2:
    arr.append(n * i)
    if (n * i) % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
    i += 1

print(*arr)