arr = list(map(int, input().split()))
cnt_arr = [0] * 6 # index 0 ~ 5

for elem in arr:
    cnt_arr[elem - 1] += 1

for i in range(1, 7):
    print(f'{i} - {cnt_arr[i-1]}')
