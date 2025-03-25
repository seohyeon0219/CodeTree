while True:
    arr = input().split()
    weight = int(arr[0])
    height = int(arr[1])
    char = arr[2]
    print(weight * height)
    if char == "C":
        break