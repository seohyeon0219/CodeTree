n = int(input())
cnt = 0

for i in range(n):
    m = int(input())

    if m % 2 != 0 and m % 3 == 0:
        cnt += m
        
print(cnt)