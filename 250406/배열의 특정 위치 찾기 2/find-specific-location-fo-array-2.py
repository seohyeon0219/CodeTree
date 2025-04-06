arr = list(map(int, input().split()))
odd_arr = []
even_arr = []

for i in range(len(arr)):
    if i % 2 == 0 or i == 0:
        odd_arr.append(arr[i])
    else:
        even_arr.append(arr[i])

sum_odd_arr, sum_even_arr = 0, 0

sum_odd_arr = sum(odd_arr)
sum_even_arr = sum(even_arr)

if sum_even_arr >= sum_odd_arr:
    print(sum_even_arr-sum_odd_arr)
else:
    print(sum_odd_arr-sum_even_arr)

