scores = input().split()
# put your python code here
correct = 0
incorrect = 3
for answer in scores:
    if answer == "I":
        incorrect -= 1
    elif answer == "C":
        if incorrect <= 0:
            break
        else:
            correct += 1

if incorrect <= 0:
    print("Game over")
    print(correct)
else:
    print("You won")
    print(correct)
