s = input()

for i in range(len(s)):
    if 'ee' in s:
        print('Yes', end=' ')
    else:
        print('No', end=' ')
    if 'ab' in s:
        print('Yes')
    else:
        print('No')
    break