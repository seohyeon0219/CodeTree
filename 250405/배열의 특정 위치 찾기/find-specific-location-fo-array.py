arr = list(map(int, input().split()))

# 짝수 번째로 입력된 값의 합
even_arr = []
for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)
    else:
        continue
print(sum(even_arr), end=" ")

# 3의 배수 번째로 입력된 값의 평균
# 3의 배수 번째 : 3, 6, 9... -> index 2, 5, 8...
# three_arr = []
# sum_arr = 0
# len_arr = 0
# sum, len = 0, 0
# # for 문 이용
# for i in range(2, 10, 3):
#     sum += arr[i]
#     len += 1
# print(f'{sum/len:.1f}')

# slicing 이용
three_arr = arr[2:10:3]
sum_arr = sum(three_arr)
len_arr = len(three_arr)
print(f'{sum_arr/len_arr:.1f}')