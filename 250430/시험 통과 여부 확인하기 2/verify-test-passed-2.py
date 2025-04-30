n = int(input())
scores = []
cnt = 0

for i in range(n):
    score = list(map(int, input().split()))
    scores.append(score)

for i in range(n):
    if sum(scores[i])/4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)