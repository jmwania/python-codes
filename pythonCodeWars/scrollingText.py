# Let's create some scrolling text!

# Your task here is to write the function scrollingText (scrolling_text in Python), 
# which takes a string, and returns an array:

# scrollingText("codewars") should return

# ["CODEWARS",
# "ODEWARSC",
# "DEWARSCO",
# "EWARSCOD",
# "WARSCODE",
# "ARSCODEW"
# "RSCODEWA",
# "SCODEWAR"]

def scrolling_text(text):
    final_list = []
    slicer = 0
    while slicer < len(text):
        final_list.append(text[slicer:].upper() + text[:slicer].upper())
        slicer += 1
    return final_list

print scrolling_text("codewars")