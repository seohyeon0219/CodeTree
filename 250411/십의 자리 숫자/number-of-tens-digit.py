arr = list(map(int, input().split()))
arr2 = []
cnt_arr = [0] * 10 # index 0~9

for elem in arr:
    if elem != 0:
        arr2.append(elem // 10)
        cnt_arr[elem // 10] += 1
    else:
        break
for i in range(1, 10):
    print(f'{i} - {cnt_arr[i]}')