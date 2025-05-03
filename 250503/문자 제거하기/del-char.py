s = list(input())
cnt = len(s)

while cnt > 1:
    n = int(input())
    if n < len(s):
        cnt -= 1
        s.pop(n)
        print(''.join(s))
    else:
        s.pop(-1)
        print(''.join(s))
    if len(s) == 1:
        break
