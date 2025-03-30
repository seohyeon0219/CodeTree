a, b = map(int, input().split())
satisfied = 0

for i in range(a, b+1):
    if (1920 % i == 0) and (2880 % i == 0):
        print(1)
        satisfied += 1
    else:
        print(0)
        satisfied += 1
    if satisfied == 1:
        break
