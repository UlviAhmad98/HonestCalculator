text = input()
words = text.split()
for word in words:
    if word.lower().startswith("https://"):
        print(word)
    elif word.lower().startswith("http://"):
        print(word)
    elif word.lower().startswith("www."):
        print(word)
    else:
        pass
    # finish the code here