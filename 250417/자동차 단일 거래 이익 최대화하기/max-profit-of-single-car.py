n = int(input()) # n년
price = list(map(int, input().split())) # n년 동안의 가격
new_price = []

for i in range(n):
    if price[i] == min(price):
        new_price = price[i:]

print(max(new_price) - min(new_price))