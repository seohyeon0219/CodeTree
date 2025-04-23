a, b = map(int, input().split())

if a % 2 == 0:
    for elem in range(a+1, b+1, 2):
        print(elem, end=' ')
else:
    for elem in range(a, b+1, 2):
        print(elem, end=' ')