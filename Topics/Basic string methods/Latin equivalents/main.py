name = input()


def normalize(name):
    # put your code here
    letter_dict = {"é": "e", "ë": "e", "á": "a", "å": "a", "œ": "oe", "æ": "ae"}
    for letter in name:
        if letter in letter_dict:
            new_name = name.replace(letter, letter_dict[letter])
            return new_name


print(normalize(name))
