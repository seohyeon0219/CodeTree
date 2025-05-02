s = input()
arr = list(s)
arr[-2], arr[1] = 'a', 'a'
print(''.join(arr))