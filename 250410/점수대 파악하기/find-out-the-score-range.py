score = list(map(int, input().split()))
cnt = [0] * 11

for elem in score:
    if elem != 0 and elem >= 10:
        section = elem // 10
        cnt[section] += 1
    else:
        continue

for i in range(10, 0, -1):
    print(f'{i*10} - {cnt[i]}')