s = list(input())
cnt = len(s)

while cnt > 1:
    n = int(input())
    cnt -= 1
    s.pop(n)
    print(''.join(s))