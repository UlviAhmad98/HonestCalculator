text = input().split()
word_list = []
for _ in text:
    if _.endswith("s"):
        word_list.append(_)
    else:
        pass
print("_".join(word_list))
