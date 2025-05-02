s = input()
arr = list(s)
elem1 = arr[0]
elem2 = arr[1]

for i in range(len(arr)):
    if arr[i] == elem2:
        arr[i] = elem1

print(''.join(arr))