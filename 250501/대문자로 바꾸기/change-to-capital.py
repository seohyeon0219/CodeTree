arr_2d = []
for _ in range(5):
    arr_1d = list(map(str, input().split()))
    arr_2d.append(arr_1d)

for i in range(5):
    for j in range(3):
        print(arr_2d[i][j].upper(), end=' ')
    print()