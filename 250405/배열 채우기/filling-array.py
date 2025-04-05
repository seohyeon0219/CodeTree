arr = list(map(int, input().split()))
arr_2 = []
reversed_arr_2 = []
for elem in arr:
    if elem != 0:
        arr_2.append(elem)
    else:
        break

for i in range(9, -1, -1):
    print(arr_2[i], end=" ")