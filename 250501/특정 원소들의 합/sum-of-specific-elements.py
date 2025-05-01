n = 4
sum = 0
arr = [list(map(int, input().split())) for _ in range(4)]

# arr[0][0]
# arr[1][0] arr[1][1]
# arr[2][0] arr[2][1] arr[2][2]
# arr[3][0] arr[3][1] arr[3][2] arr[3][3]

for i in range(n-3):
    sum += arr[n-4][i]
for i in range(n-2):
    sum += arr[n-3][i]
for i in range(n-1):
    sum += arr[n-2][i]
for i in range(n):
    sum += arr[n-1][i]

print(sum)
