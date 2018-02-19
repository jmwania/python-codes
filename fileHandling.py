myfile = open("/home/jwoche@SamaDc.corp/Desktop/myfile.txt", "w")
text_written = myfile.write("I wrote this line to this file using Python")
print text_written
myfile.close()

# readfile = open("/home/jwoche@SamaDc.corp/Desktop/myfile.txt", "r")
# for line in readfile:
# 	print line
# readfile.close()
