a = list(input())
b = list(input())
new_a, new_b = [], []

for i in range(len(a)):
    if a[i].isdigit() == True:
        new_a.append(a[i])
    else:
        continue

for i in range(len(b)):
    if b[i].isdigit() == True:
        new_b.append(b[i])
    else:
        continue

str_a = ''.join(new_a)
str_b = ''.join(new_b)
print(int(str_a) + int(str_b))