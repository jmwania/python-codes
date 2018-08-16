"""Function for pig latin"""


def pig_latin_converter(word):
    """Function to convert given word to pig latin"""

    # Check for empty string and alphabetical characters
    if word.isalpha() and len(word) > 0:
        new_word = word.lower()
        first_consonants = ""

        # In a case where the first letter is a vowel
        first = new_word[:1]
        if first in 'aeiou':
            return new_word + "way"

        # In a case where the first letter(s) is/are consonants
        for char in new_word:
            if char in 'bcdfghjklmnpqrstvwxyz':
                first_consonants += char
            if char in 'aeiou':
                break
        # Return desired output
        return new_word[len(first_consonants):] + first_consonants + "ay"

    else:
        return "String should not be empty"

    # Alternatively

    # def pigLatin(word):
    # w = word.lower()
    # vowels = "aeiou"
    # pig = "way"
    # cpig = "ay"

    # if w[0] not in vowels:
    #     for index, char in enumerate(w):
    #         if char in vowels:
    #             return w[index:] + w[0:index] + cpig
    # else:
    #     return w + pig
