a, b = map(int, input().split())
share_arr = [0] * b

while a > 1:
    share_arr[a % b] += 1
    a //= b

    if a == 0:
        break

print(sum(elem ** 2 for elem in share_arr))