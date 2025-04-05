arr = list(map(float, input().split()))
sum, len, avg = 0, 0, 0
arr_2 = []

for elem in arr:
    if elem != 0:
        arr_2.append(elem)
    else:
        break

for elem in arr_2:
    sum += elem
    len += 1

avg = sum / len
print(f'{int(sum)} {avg:.1f}')