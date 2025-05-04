arr = []
new_arr1 = []
new_arr2 = []
new_arr3 = []

while True:
    a = input()
    if a == 'END':
        break
    arr.append(a)

new_arr1 = list(arr[0])
new_arr2 = list(arr[1])
new_arr3 = list(arr[2])

print(''.join(new_arr1[::-1]))
print(''.join(new_arr2[::-1]))
print(''.join(new_arr3[::-1]))

