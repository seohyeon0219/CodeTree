month = int(input())
# 30 : 4,6,9,11
# 31 : 1,3,5,7,8,10,12
# 28 : 2

if month in [4,6,9,11]:
    print(30)
elif month in [1,3,5,7,8,10,12]:
    print(31)
else:
    print(28)