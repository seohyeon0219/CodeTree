# 환자 상태 입력받기
con1, tem1 = input().split()
con2, tem2 = input().split()
con3, tem3 = input().split()

# int로 변환
tem1, tem2, tem3 = int(tem1), int(tem2), int(tem3)

# 상태에 따라서 배열에 저장
A, B, C, D = 0, 0, 0, 0
con_arr = [con1, con2, con3]
tem_arr = [tem1, tem2, tem3]

for i in range(3):
    if con_arr[i] == 'Y':
        if tem_arr[i] >= 37:
            A += 1
        else:
            C += 1
    else:
        if tem_arr[i] >= 37:
            B += 1
        else:
            D += 1

print(A, B, C, D, end=' ')

if A >= 2:
    print('E')