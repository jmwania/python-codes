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
		return '{} {}'.format(self.first,self.last)

	#Accessing our class variable, raise_amount
	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amount)

	#Modifying class variables using a class method
	#This is called a decorator. Notifies that this is not a regular method.
	@classmethod
	def set_raise_amnt(cls,amount):
		cls.raise_amount = amount

	#This is how you'd use a class method as an alternative constructor
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)

	#Jumping to static methods
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	#Two other special methods besides __init__
	def __repr__(self):
		return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

	def __str__(self):
		#This returns 'None' under fullname for some reason. Yet to find out why!
		#Got it! The fullname() method was printing instead of returning
		return "Employee('{} - {}')".format(self.full_name(),self.email)


#Implementing inheritance
class Developer(Employee):

	raise_amount = 1.10
	def __init__(self,first,last,pay,prog_lang):
		Employee.__init__(self,first,last,pay)
		#For some reason, this method didn't work
		#super().__init__(first,last,pay)
		self.prog_lang = prog_lang
class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		Employee.__init__(self,first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print_emps(self):
		for emp in self.employees:
			print '--->', emp.full_name()




#Let's add some employees to our company
emp1 = Employee('Jillo','Abdullahi',60000)
emp2 = Employee('Juma','Woche',20000)

#Let's appraise emp1 using the class method
print emp1.pay
emp1.apply_raise()
print emp1.pay

#Some strings sent to us
emp1_string = 'John-Doe-70000'

#Creating a new employee using the alternative constructor
new_emp1 = Employee.from_string(emp1_string)

#Print out some values to see if this works.
print new_emp1.full_name()
print new_emp1.pay

#Checking day using our static method
import datetime
my_date = datetime.date(2018,2,6)

print Employee.is_workday(my_date)

#Working with developer
#print (help(Developer))

#Get some new developers into the company
dev1 = Developer("John","Doe",100000,"Python")
dev2 = Developer("Joh","Doe",200000,"Python")
dev3 = Developer("Jo","Doe",300000,"Python")
print dev1.email
dev1.apply_raise()
print dev1.pay

#Adding some managers to the company
mgr_1 = Manager("John","Sue",500000,[dev1])
print mgr_1.email

mgr_1.add_emp(dev2)
mgr_1.remove_emp(dev2)
mgr_1.print_emps()

#Using isinstance
print isinstance(mgr_1,Manager)

#Using issubclass
print issubclass(Developer,Employee)

#Print object in a more meaningful way using __repr__()/__str__()
#__repr__() is the fallback special/dunder method in case __str__() is not defined
print emp1







