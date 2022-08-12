word = input()

for letter in word:
    if letter.islower is False:
        letter = letter.replace(letter.upper(), "_" + letter.lower())
print(word)
