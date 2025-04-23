b, a = map(int, input().split())

if b % 2 == 0:
    for elem in range(b-1, a-1, -2):
        print(elem, end=' ')
else:
    for elem in range(b, a-1, -2):
        print(elem, end=' ')