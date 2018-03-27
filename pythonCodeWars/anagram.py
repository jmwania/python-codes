# https://www.codewars.com/kata/anagram-detection/train/python
def is_anagram(test, original):
    return True if sorted(test.lower()) == sorted(original.lower()) else False


print (is_anagram('Creative', 'Reactive'))