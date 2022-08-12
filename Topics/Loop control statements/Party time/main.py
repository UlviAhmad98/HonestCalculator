
guest_list = []
while True:
    guests = input()
    if guests == ".":
        break
    else:
        guest_list.append(guests)

print(guest_list)
print(len(guest_list))
