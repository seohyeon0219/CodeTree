a = input()

if len(a) % 2 == 0:
    for elem in a[-1:0:-2]:
        print(elem, end='')
else:
    for elem in a[-2:0:-2]:
        print(elem, end='')