grade = float(input())
max_score = int(input())
if 0.9 * max_score <= grade <= max_score:
    print("A")
elif 0.8 * max_score <= grade < 0.9 * max_score:
    print("B")
elif 0.7 * max_score <= grade < 0.8 * max_score:
    print("C")
elif 0.6 * max_score <= grade < 0.7 * max_score:
    print("D")
else:
    print("F")
