a, b = map(int, input().split())
prod = 1
# a를 b번 곱하기 
for i in range(b):
    prod *= a

print(prod)