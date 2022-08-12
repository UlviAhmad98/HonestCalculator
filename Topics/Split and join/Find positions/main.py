# put your python code here
values = input().split()
x = str(input())
new_list = []
for index, value in enumerate(values):
    if value == x:
        new_list.append(str(index))
    else:
        pass

if x in values:
    print(" ".join(new_list))
else:
    print("not found")
