arr = list(map(int, input().split()))
cnt_arr = [0] * 6 # index 0,1,2,3,4,5

for elem in arr:
    cnt_arr[elem-1] += 1

for i in range(6):
    print(f'{i+1} - {cnt_arr[i]}')