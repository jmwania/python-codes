#Write simple .camelCase method (camel_case function in PHP or CamelCase in C#) for strings. 
#All words must have their first letter capitalized without spaces.

def to_camel_case(string):
    if string == "":
        return ""
    else:
        new_list = []
        for word in string.split(" "):
            if word == string.split(" ")[0]:
                new_list.append(word)
            else:
                new_list.append(word.capitalize())
    return "".join(new_list)


print (to_camel_case("test case"))
