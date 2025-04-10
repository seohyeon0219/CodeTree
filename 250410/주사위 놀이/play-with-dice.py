arr = map(int, input().split())
cnt_arr = [0] * 6
cnt = 0

for elem in arr:
    cnt_arr[elem-1] += 1

for i in cnt_arr:
    print(f'{i} - {cnt_arr[i-1]}')