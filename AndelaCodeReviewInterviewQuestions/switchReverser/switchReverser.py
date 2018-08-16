"""Switch reverser function"""


def switch_reverser(myList):
    """Function to reverse/convert list items to uppercase"""
    integer_list = []
    word_only_list = []
    # check each item in the list and append to corresponding list
    for item in myList:
        if isinstance(item, int):
            integer_list.append(item)
        elif isinstance(item, str):
            word_only_list.append(item)

    # Compare with original list and return desired outputs
    if len(integer_list) == len(myList):
        return myList[::-1]
    elif len(word_only_list) == len(myList):
        upper_case_list = []
        for word in word_only_list:
            upper_case_list.append(word.upper())
        return upper_case_list
    else:
        return myList

    # check out simpler code on stackoverflow

    # def switch(mylist):
    #     if all(isinstance(n, int) for n in mylist):
    #             return mylist[::-1]

    #     elif all(isinstance(n, str) for n in mylist) and all(n.isalpha() for n in mylist):
    #             return [n.upper() for n in mylist]

    #     else:
    #             return mylist
