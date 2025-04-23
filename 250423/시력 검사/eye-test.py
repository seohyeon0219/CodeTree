right_eye = float(input())
left_eye = float(input())

if right_eye >= 1.0 and left_eye >= 1.0:
    print('High')
elif right_eye >= 0.5 and left_eye >= 0.5:
    print('Middle')
else:
    print('Low')