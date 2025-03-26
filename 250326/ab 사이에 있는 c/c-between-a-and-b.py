arr = input().split()
a, b = int(arr[0]), int(arr[1])

satisfied = False
for i in range(a, b+1):
    if i % 2 == 0:
        satisfied = True

if satisfied == True:
    print("Exists")
else:
    print("Not exists")