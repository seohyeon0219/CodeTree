n = int(input())
arr = []
i = 1

while i <= n:
    arr.append(int(input()))

    i += 1

for i in range(0,n,1):
    if arr[i] % 2 != 0 and arr[i] % 3 == 0:
        print(arr[i])


# n = int(input())

# for i in range(n):
#     n = int(input())
#     if n % 2 == 1 and n % 3 == 0:
#         print(n)