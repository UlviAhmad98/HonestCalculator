value_list = []
while True:
    value = input()
    if value == ".":
        break
    else:
        value_list.append(float(value))

print(min(value_list))
