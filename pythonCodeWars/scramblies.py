import re
def scramble(s1, s2):
    # pattern = r"{}".format("".join(sorted(s2)))
    # if re.match(pattern,"".join(sorted(s1))):
    #     return True
    # else:
    #     return False


    # for string in s2.lower():
    #     if string not in s1.lower():
    #         return False
    # else:
    #     return True

    # Above methods didn't work but these ones did:
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

    # Alternative method:
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


print scramble('scriptingjava', 'javascript')

