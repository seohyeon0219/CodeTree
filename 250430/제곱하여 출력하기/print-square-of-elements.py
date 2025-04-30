n = int(input())
arr = list(map(int, input().split()))
print(*[elem ** 2 for elem in arr])