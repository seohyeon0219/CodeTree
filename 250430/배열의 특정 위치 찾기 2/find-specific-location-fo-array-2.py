arr = list(map(int, input().split()))

even_sum = sum(arr[i] for i in range(1, 10, 2))
odd_sum = sum(arr[i] for i in range(0, 10, 2))

print(abs(even_sum - odd_sum))