s = list(input())

# 방법 1
for i in s:
    if i.isupper(): # 대문자이면
        print(i.lower(), end='')
    else: # 소문자이면
        print(i.upper(), end='')

# # 방법 2
# for i in range(len(s)):
#     if s[i].isupper():
#         print(s[i].lower(), end='')
#     else:
#         print(s[i].upper(), end='')
# 
# # 방법 3
# for i in s:
#     if i.isupper():
#         i = i.lower()
#         print(i, end='')
#     else:
#         i = i.upper()
#         print(i, end='')

