arr = list(map(int, input().split()))
arr_2 = []
reversed_arr_2 = []
for elem in arr:
    if elem != 0:
        arr_2.append(elem)
    else:
        break

reversed_arr_2 = arr_2[::-1]

for elem in reversed_arr_2:
    print(elem, end=" ")
