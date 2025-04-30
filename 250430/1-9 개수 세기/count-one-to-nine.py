n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0] * 9

for elem in arr:
    cnt_arr[elem-1] += 1

print(*cnt_arr, sep='\n')

