height, weight = map(int, input().split())
b = (weight) / (height/100)**2
print(f'{b:.0f}')
if b >= 25:
    print('Obesity')