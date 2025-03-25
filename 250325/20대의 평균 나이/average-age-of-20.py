sum = 0
cnt = 0

while True:
    n = int(input())
    if n < 30 and n >= 20:
        sum += n
        cnt += 1
    else:
        break

print(f'{sum / cnt :.2f}')