n = int(input())
cnt = 1

while True:
    n = n // 2
    cnt += 1
    if n == 2:
        break

print(cnt)