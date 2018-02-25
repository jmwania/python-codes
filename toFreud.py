def to_freud(sentence):
	#Replace the instance of each word with "sex"
	new_str = sentence.split(" ")
	for word in range(len(new_str)):
		new_str[word] = "sex"
	return " ".join(new_str)

  


print to_freud("This is a longer test")