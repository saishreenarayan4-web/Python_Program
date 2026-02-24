#setter and getter
class Student:
	def __init__(self):
		self.name = ""
	def setName(self,name):
		self.name=name 
	def getName(self):
		return self.name 

#Object Creation
s1=Student()


#Set value
s1.setName("sai")


#Getvalue
print("Student name:",s1.getName())
#print("Student name:",s1.getName())