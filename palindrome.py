import re
def is_palindrome(string):
	"""A function that returns true if a  string is a palidrome"""

	#Test if input is a string
	if type(string) != str:
		return False
	#Convert the string to lowercase
	string = string.lower()

	#Remove punctuations and spaces using regex
	string = re.sub("\W+","",string)

	#Reverse the string:
	count = len(string)
	new_str = ""
	while count > 0:
		new_str +=string[count-1]
		count-=1

	#Check if string is a palidrome and return true or false
	if new_str == string:
		return True
	else:
		return False

if __name__ == '__main__':
	print is_palindrome(123321)