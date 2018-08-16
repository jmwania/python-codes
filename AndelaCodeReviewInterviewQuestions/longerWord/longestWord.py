"""Longer word function"""


def longer_word(str1, str2):
    """Function to test two strings using length"""
    if not isinstance(str1, str) or not isinstance(str2, str):
        return "All inputs must be string"
    if len(str1) == len(str2):
        return str1 + "\n" + str2
    return str1 if len(str1) > len(str2) else str2

print(longer_word("Mammoth", "Mammoth"))
