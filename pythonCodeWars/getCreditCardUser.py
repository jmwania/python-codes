def get_issuer(number):
  number_list = str(number)
  first = number_list[0]
  first_two = number_list[0:2]
  first_four = number_list[0:4]
  length = len(number_list)

  if first_two == '34' or first_two == "37" and length == 15:
    return "AMEX"
  elif first_four == '6011' and length == 16:
    return "Discover"
  elif first_two == '51' or first_two == '52' or first_two == '53' or first_two == '54' or first_two == '55' and length == 16:
    return "Mastercard"
  elif first == '4' and (length == 13 or length == 16):
    return "VISA"
  else:
    return "Unknown"

#Alternatively
# def get_issuer(number):
#     s = str(number)
#     return ("AMEX"       if len(s)==15 and s[:2] in ("34","37") else
#             "Discover"   if len(s)==16 and s.startswith("6011") else
#             "Mastercard" if len(s)==16 and s[0]=="5" and s[1] in "12345" else
#             "VISA"       if len(s) in [13,16] and s[0]=='4' else
#             "Unknown")
  

print (get_issuer(9111111111111111))