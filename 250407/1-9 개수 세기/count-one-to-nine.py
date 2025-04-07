n = int(input())
arr = list(map(int, input().split()))

cnt = 0
cnt_arr = [0] * 9

for elem in arr:
    cnt_arr[elem-1] += 1

for i in range(1, 9):
    print(cnt_arr[i])