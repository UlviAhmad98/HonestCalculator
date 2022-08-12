# put your python code here

a = int(input())
b = int(input())
value_list = []
for value in range(a, (b + 1)):
    if value % 3 == 0:
        value_list.append(value)

print(sum(value_list) / len(value_list))
