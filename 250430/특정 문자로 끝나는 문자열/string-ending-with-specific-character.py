arr = [input() for _ in range(10)]
a = input()
cnt = 0

for i in range(len(arr)):
    if arr[i][-1] == a:
        print(arr[i])
        cnt += 1
if cnt == 0:
    print('None')