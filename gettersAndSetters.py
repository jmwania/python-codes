class Employee:

	"""An employee class to help us with OOP
	Tutorial on YouTube courtesy of Corey Schafer"""
	#These two are class variables
	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self,first,last,pay):

		#These are instance variables"""
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@email.com"

		#Increment the number of employees by one everytime a new employee is instantiated.
		Employee.num_of_emps += 1

	def full_name(self):
		#Found this to be fancy for formatted output.
		#Don't forget to add self when referring to variables
		print '{} {}'.format(self.first,self.last)