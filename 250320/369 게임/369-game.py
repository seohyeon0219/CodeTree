n = int(input())
i = 1

while i <= n:
    if i % 3 == 0:
        print(0, end=' ')
        i += 1
    elif i % 10 == (3 or 6 or 9):
        print(0, end=' ')
        i += 1
    else:
        print(i, end=' ')
        i += 1
        # 3 6 9 13 16 19 