a,b = map(int,input().split())

if a > 0:
    for i in range(b):
        print(a, end='')
        i += 1
else:
    print(0)