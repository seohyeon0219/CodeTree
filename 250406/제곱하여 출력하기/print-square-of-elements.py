n = int(input())
arr = list(map(int, input().split()))
arr_2 = [elem ** 2 for elem in arr]

for elem in arr_2:
    print(elem, end=' ')

# for i in range(len(arr_2)):
#     print(arr_2[i], end=' ')