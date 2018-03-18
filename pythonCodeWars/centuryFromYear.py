# https://www.codewars.com/kata/century-from-year/train/python
def century(year):
    if year < 101:
        return 1
    elif len(str(year)) == 3:
        if int(str(year)[1:]) > 1:
            return int(str(year)[:1])+1
        else:
            return int(str(year)[:1])
    elif len(str(year)) == 4:
        if int(str(year)[2:]) > 0:
            return int(str(year)[:2]) + 1
        else:
            return int(str(year)[:2])

print century(22)



#Shortcut:
 # return (year + 99) // 100