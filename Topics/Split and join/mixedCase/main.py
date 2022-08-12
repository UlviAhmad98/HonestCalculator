text = input().split()
mixed_case = ""
for word in text:
    if text.index(word) != 0:
        mixed_case += word.capitalize()
    else:
        mixed_case += word
print(mixed_case)