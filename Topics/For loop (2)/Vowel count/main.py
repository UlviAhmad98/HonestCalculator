string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0
for vowel in vowels:
    for word in string:
        if vowel in word:
            counter += 1
print(counter)
