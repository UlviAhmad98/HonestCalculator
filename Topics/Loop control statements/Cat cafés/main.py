names = []
numbers = []

while True:
    cafe = input().split()

    if cafe[0] == "MEOW":
        max_val = max(numbers)
        print(names[numbers.index(max_val)])
        break
    else:
        name = cafe[0]
        number = int(cafe[1])
        names.append(name)
        numbers.append(number)
