# put your python code here
value_list = []
square_list = []
while True:
    value = int(input())
    value_list.append(value)
    square_list.append(value ** 2)
    if value_list[0] == 0:
        print("0")
        break
    elif sum(value_list) == 0:
        print(sum(square_list))
        break
    else:
        pass
