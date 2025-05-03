s = list(input())
cnt = len(s)

while cnt > 1:
    n = int(input())
    if n < len(s):
        cnt -= 1
        s.pop(n)
        print(''.join(s))
    if n >= len(s):
        s.pop(-1)
        print(''.join(s))
