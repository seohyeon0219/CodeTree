a, b = map(int, input().split())
arr = [a, b]

for i in range(2, 10):
    arr.append(arr[-2] + arr[-1])

print(*(elem % 10 if elem >= 10 else elem for elem in arr))