n = int(input())
sum, m, cnt = 0, 0, 0

for i in range(n):
    m = int(input())
    sum += m
    cnt += 1

print(f'{sum} {sum/cnt:.1f}')