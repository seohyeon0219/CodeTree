arr = list(map(int, input().split()))
i = arr.index(0)
arr = arr[:i]
arr = [elem // 10 if elem >= 10 else 0 for elem in arr]
cnt_arr = [0] * 10

for elem in arr:
    cnt_arr[elem] += 1

for i in range(1, 10):
    print(f'{i} - {cnt_arr[i]}')
