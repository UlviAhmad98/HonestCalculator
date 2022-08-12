height = int(input())
n = 1
for _ in range(height):
    print((n * "#").center(height * 2 - 1))
    n += 2
