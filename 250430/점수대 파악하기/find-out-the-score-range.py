arr = list(map(int, input().split()))
i = arr.index(0)
arr = arr[:i]
arr = [elem // 10 for elem in arr]

cnt_arr = [0] * 11 # index 0~9

for elem in arr:
    cnt_arr[elem] += 1

for i in range(10, 0, -1):
    print(f'{i*10} - {cnt_arr[i]}')

