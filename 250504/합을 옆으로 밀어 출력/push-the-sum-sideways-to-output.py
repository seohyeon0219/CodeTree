n = int(input())
arr = []
sum = 0

for _ in range(n):
    a = int(input())
    arr.append(a)

for i in arr:
    sum += i

sum = str(sum)
print(sum[1:] + sum[0])