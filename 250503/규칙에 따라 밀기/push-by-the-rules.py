a = input()
arr = input()

for elem in arr:
    if elem == 'L':
        arr = a[1:] + a[0]
    else:
        arr = a[-1] + a[:-1]
print(arr)