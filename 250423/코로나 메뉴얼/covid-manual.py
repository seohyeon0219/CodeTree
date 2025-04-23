a_con, a_temp = map(str, input().split())
b_con, b_temp = map(str, input().split())
c_con, c_temp = map(str, input().split())

a_temp, b_temp, c_temp = int(a_temp), int(b_temp), int(c_temp)

cnt = 0

if a_con == 'Y':
    if a_temp >= 37:
        cnt += 1
if b_con == 'Y':
    if b_temp >= 37:
        cnt += 1
if c_con == 'Y':
    if c_temp >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')

