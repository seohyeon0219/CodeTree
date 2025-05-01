n = int(input())
str = input().split()
str = ''.join(str)

for i in range(0,len(str),5):
    print(str[i:i+5])

