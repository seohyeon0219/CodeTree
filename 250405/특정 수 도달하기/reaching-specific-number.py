arr = list(map(int, input().split()))
arr_250 = []
sum, len, avg = 0, 0, 0

for elem in arr:
    if elem < 250:
        arr_250.append(elem)
    else:
        break

for i in arr_250:
    sum += i
    len += 1

avg = sum / len

print(f'{sum} {avg:.1f}')