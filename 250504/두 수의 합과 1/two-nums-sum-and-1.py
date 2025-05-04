a, b = map(int, input().split())
sum = a + b
sum = str(sum)
cnt = 0

for i in sum:
    if i == '1':
        cnt += 1

print(cnt)