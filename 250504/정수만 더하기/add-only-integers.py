s = list(input())
new_s = []
sum = 0

for i in s:
    if i.isdigit() == True:
        new_s.append(i)
    else:
        pass

for i in new_s:
    i = int(i)
    sum += i

print(sum)