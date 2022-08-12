# put your python code here
value_list = []
while True:
    value = int(input())
    if value < 10:
        continue
    elif value > 100:
        break
    else:
        value_list.append(value)
for _ in value_list:
    print(_)
