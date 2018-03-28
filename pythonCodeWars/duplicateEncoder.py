# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
from collections import Counter
def duplicate_encode(word):
    letter_counts = Counter(word.lower())
    new_string = ""
    for letter in word.lower():
        if letter_counts[letter] == 1:
            new_string += '('
        elif letter_counts[letter] > 1:
            new_string += ')'
    return new_string



