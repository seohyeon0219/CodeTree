cond1, temp1 = input().split()
cond2, temp2 = input().split()
cond3, temp3 = input().split()

temp1, temp2, temp3 = int(temp1), int(temp2), int(temp3)

hops_arr = [0] * 4
cond = [cond1, cond2, cond3]
temp = [temp1, temp2, temp3]

for i in range(3):
    if cond[i] == 'Y':
        if temp[i] >= 37:
            hops_arr[0] += 1
        else:
            hops_arr[2] += 1
    else:
        if temp[i] >= 37:
            hops_arr[1] += 1
        else:
            hops_arr[3] += 1

if hops_arr[0] >= 2:
    hops_arr.append('E')

print(*hops_arr)