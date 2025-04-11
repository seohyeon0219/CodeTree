n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0] * 9 # index : 0~8 총 9개

for elem in arr:
    cnt_arr[elem-1] += 1 # 1은 0에 저장,,,,,9는 8에 저장

for i in range(1, 10): # 0~9
    print(cnt_arr[i-1])