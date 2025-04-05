n = int(input())
arr_scores = list(map(float, input().split()))
sum, len, avg = 0, 0, 0

for elem in arr_scores:
    sum += elem
    len += 1

avg = sum / len
print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")