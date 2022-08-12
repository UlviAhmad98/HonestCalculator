import random
number = int(input())
division_count = 0
for i in range(1, number+1):
    if number % i == 0:
        division_count += 1
    else:
        pass

if division_count == 2:
    print("This number is prime")
else:
    print("This number is not prime")
