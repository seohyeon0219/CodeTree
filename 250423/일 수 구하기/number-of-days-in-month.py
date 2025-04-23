month = int(input())

if month % 2 == 0:
    if month == 2:
        print(28)
    else:
        print(30)
else:
    print(31)