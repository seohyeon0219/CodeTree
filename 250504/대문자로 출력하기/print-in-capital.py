s = list(input())
new_s = []

for i in s:
    if i.isalpha() == True:
        new_s.append(i.upper())
    else:
        continue

for i in new_s:
    print(i, end='')