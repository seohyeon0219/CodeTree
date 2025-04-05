n = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]
even_arr = []

for elem in reversed_arr:
    if elem % 2 == 0:
        even_arr.append(elem)
    else:
        continue

for elem in even_arr:
    print(elem, end=" ")
