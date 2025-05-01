arr_2d = []
width_sum = [0] * 2
height_sum = [0] * 4
total_sum = 0

for _ in range(2):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

# 가로 합
# for j in range(4):
#     width_sum[0] += arr_2d[0][j]
#     width_sum[1] += arr_2d[1][j]
#     j += 1

for j in range(4):
    for i in range(2):
        width_sum[i] += arr_2d[i][j] / 4

# 세로 합
# for i in range(2):
#     height_sum[0] += arr_2d[i][0]
#     height_sum[1] += arr_2d[i][1]
#     height_sum[2] += arr_2d[i][2]
#     height_sum[3] += arr_2d[i][3]
#     i += 1

for i in range(2):
    for j in range(4):
        height_sum[j] += arr_2d[i][j] / 2

# 전체 합
for i in range(2):
    for j in range(4):
        total_sum += arr_2d[i][j]
print(*width_sum)
print(*height_sum)
print(f'{total_sum/8:.1f}')
