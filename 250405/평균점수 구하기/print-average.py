arr_scores = list(map(float, input().split()))
sum, len, avg = 0, 0, 0

for elem in arr_scores:
    sum += elem
    len += 1

avg = sum / len
print(f'{avg:.1f}')