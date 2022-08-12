column = int(input())
row = int(input())

if column in (1, 8) and row in (1, 8):
    print("3")
elif column in (1, 8) and (1 < row < 8):
    print("5")
elif (1 < column < 8) and row in (1, 8):
    print("5")
else:
    print("8")
