value = float(input())

if value < 2:
    print("Analytic")
elif 2 <= value <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
