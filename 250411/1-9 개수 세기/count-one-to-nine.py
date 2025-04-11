n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0] * 10

for elem in arr:
    cnt_arr[elem - 1] += 1

for i in range(10): # 0 ~ 9 -> 10개
    print(cnt_arr[i])