n = int(input())
arr = [input() for _ in range(n)]

# 문자열 길이의 합
len_arr = 0

for elem in arr:
    len_arr += len(elem)

# 첫 번째 문자로 a가 몇 번 나왔는지
count_a = 0

for i in range(len(arr)):
    if arr[i][0] == 'a':
        count_a += 1

print(len_arr, count_a)
