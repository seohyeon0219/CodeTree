A, B = map(int, input().split())
arr = []
cnt = [0] * 10
sum = 0

while A != 0:
    arr.append(A % B)
    A //= B

for elem in arr:
    cnt[elem] += 1

for i in range(len(cnt)):
    sum += cnt[i] ** 2

print(sum)