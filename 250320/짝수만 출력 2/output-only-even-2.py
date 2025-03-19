b,a = map(int,input().split())

while a <= b:
    if b % 2 == 0:
        print(b, end=' ')
        b -= 2
    else:
        print(b+1, end=' ')
        b -= 2
