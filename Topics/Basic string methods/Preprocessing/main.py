# text = input()
#
# new_text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
# print(new_text)

text = input()

symbols = [",", ".", "!", "?"]

for _ in symbols:
    text = text.replace(_, "")

print(text.lower())
