sum = 0
a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        sum += i

print(sum)