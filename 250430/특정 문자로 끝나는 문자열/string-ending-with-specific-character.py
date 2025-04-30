arr = [input() for _ in range(10)]
a = input()

for i in range(len(arr)):
    if arr[i][-1] == a:
        print(arr[i])