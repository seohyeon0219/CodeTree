s = input()
cnt_ee, cnt_eb = 0, 0

for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        cnt_ee += 1
    if s[i:i+2] == 'eb':
        cnt_eb += 1

print(cnt_ee, cnt_eb)