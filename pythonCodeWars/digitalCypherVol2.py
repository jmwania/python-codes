#https://www.codewars.com/kata/digital-cypher-vol-2/train/python
def decode(code, key):
    code_dict = {}
    count = 1
    #Generate a list of alphabets:
    alphabets = map(chr,range(97,123))
    
    #Generate our code list:
    while count < 26:
        for letter in alphabets:
            code_dict[str(count)] = letter
            count+=1
    
    #Decode our message:
    counter = 0
    decode = []
    for num in code:
        decode.append(num - int(str(key)[counter]))
        counter+=1
        if counter == len(str(key)):
            counter = 0
    
    #Print our decoded message:
    message = ""
    for num in decode:
        message += code_dict[str(num)]
    return message




print decode([20, 12, 18, 30, 21], 1939) #scout
#decode = 19  3 15 21 20