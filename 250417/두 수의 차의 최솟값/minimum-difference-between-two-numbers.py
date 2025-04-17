n = int(input())
arr = list(map(int, input().split()))
minus = []

for i in arr:
    for j in arr:
        if i > j:
            minus.append(i-j)
        else:
            continue

print(min(minus))

