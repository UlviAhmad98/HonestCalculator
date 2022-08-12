text = input()
new_text = ""
for _ in text:
    if _.islower() is False:
        new_text += "_"
        new_text += _.lower()
    else:
        new_text += _

print(new_text)
