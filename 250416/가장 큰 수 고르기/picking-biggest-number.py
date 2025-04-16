arr = list(map(int, input().split()))
max_arr = 0

for elem in arr:
    if elem > max_arr:
        max_arr = elem

print(max_arr)