n = int(input())
list = []

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    elif i % 10 == 5:
        continue
    elif i % 3 == 0 and i % 9 != 0:
        continue
    else:
        list.append(i)

list.sort()

for j in list:
    print(j, end = ' ')