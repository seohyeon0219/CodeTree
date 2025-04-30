n = int(input())
arr = list(map(int, input().split()))

print(*(elem for elem in arr if elem % 2 == 0))