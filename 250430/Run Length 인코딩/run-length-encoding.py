A = input()

# Please write your code here.a = input()

# 순서대로 들어있는 소문자를 저장할 리스트 arr 만들기
arr = [a[0]]

for i in range(len(a)):
    if arr[-1] != a[i]:
        arr.append(a[i])
    else:
        continue
print(arr)
# 리스트 arr의 소문자 개수를 저장할 리스트 cnt 만들기
cnt = [0] * len(arr)

for i in range(len(a)):
    for j in range(len(arr)):
        if a[i] == arr[j]:
            cnt[j] += 1


print(cnt)
