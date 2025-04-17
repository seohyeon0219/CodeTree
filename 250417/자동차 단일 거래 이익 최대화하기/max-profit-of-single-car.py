n = int(input())
price_arr = list(map(int, input().split()))

min_val = price_arr[0]

for i in range(n):
    if min_val > price_arr[i]:
        min_val = price_arr[i]

print(max(price_arr) - min_val)
