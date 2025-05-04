s = list(input())
new_s = []

for i in s:
    if i.isalpha():
        new_s.append(i.lower())
    elif i.isdigit():
        new_s.append(i)

for i in new_s:
    print(i, end='')