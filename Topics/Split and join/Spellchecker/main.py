dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()
word_list = []
correct = 0
for word in sentence:
    if word not in dictionary:
        word_list.append(word)
    else:
        correct += 1

if correct == len(sentence):
    print("OK")
else:
    print("\n".join(word_list))
