s = input()
n = len(s)
new_s = 0

for i in range(len(s)+1):
    new_s = s[-i:] + s[:-i]
    print(new_s)