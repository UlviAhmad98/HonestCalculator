mean = []
while True:
    value = input()
    if value != ".":
        mean.append(int(value))
    elif value == ".":
        print(sum(mean) / len(mean))
        break
