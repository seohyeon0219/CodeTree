arr = list(map(int, input().split()))
arr_2 = []
sum, len = 0, 0

for elem in arr:
    if elem != 0:
        if elem % 2 == 0:
            arr_2.append(elem)
        else:
            continue
    else:
        break

for elem in arr_2:
    sum += elem
    len += 1

print(len, sum)