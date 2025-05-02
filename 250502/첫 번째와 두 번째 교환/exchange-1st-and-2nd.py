s = input()
arr = list(s)
a = arr[0]
b = arr[1]

for i in range(len(arr)):
    if arr[i] == a:
        arr[i] = b
    elif arr[i] == b:
        arr[i] = a

print(''.join(arr))