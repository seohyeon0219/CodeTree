n = int(input())
arr = list(map(int, input().split()))

cnt = 0
cnt_arr = [0] * 9 # index 0~8 총 9개

for elem in arr:
    cnt_arr[elem - 1] += 1 # 1번째 값 -> 0번째 index에 저장해야 하기에

for i in range(0, 9):
    print(cnt_arr[i])