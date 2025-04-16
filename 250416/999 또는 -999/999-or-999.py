arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        new_arr = arr[:i]

# print(max(new_arr), min(new_arr))

val = new_arr[0]
min_val, max_val = 0, 0

for elem in new_arr:
    if elem <= val:
        min_val = elem
    if elem >= val:
        max_val = elem

print(max_val, min_val)

