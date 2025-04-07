arr = list(map(int, input().split()))
cnt_arr = [0] * 6 # index 0~5
cnt = 0

for elem in arr:
    cnt_arr[elem - 1] += 1

for i, elem in enumerate(cnt_arr):
    print(f'{i+1} - {elem}')

# for i in range(len(cnt_arr)):
#     print(f'{i+1} - {cnt_arr[i]}')