import sys

n = int(input())
arr = list(map(int, input().split()))
min = sys.maxsize
min_cnt = 0

for elem in arr:
    if elem < min:
        min = elem

print(min, arr.count(min))
