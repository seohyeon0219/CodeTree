a1, a2 = map(int, input().split())
arr = [a1, a2]

while len(arr) < 10:
    arr.append(arr[-1] + 2 * arr[-2])

print(*arr)