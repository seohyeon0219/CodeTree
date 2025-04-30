given_str = input()
n = int(input())

for elem in given_str[-1:-n-1:-1]:
    print(elem, end='')