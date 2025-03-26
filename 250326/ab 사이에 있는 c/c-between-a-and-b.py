satisfied = False

a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i % c == 0:
        satisfied = True

if satisfied == True:
    print("YES")
else:
    print("NO")