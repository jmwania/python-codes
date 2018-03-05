#Trying to correct some code

def weather_info (temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius (temperature):
  celsius = (temperature - 32) * (5.0/9.0)
  return celsius



# print convertToCelsius(50)
print weather_info(56)