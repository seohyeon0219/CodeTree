height, weight = map(int, input().split())
b = int(weight / (height/100) ** 2)

print(b)
if b >= 25:
    print('Obesity')