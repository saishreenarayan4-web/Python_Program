class Student:
	clg="iter"                #class variable common for all object
	def __init__(self):
		self.name="muna"       #instance variable  object data
		self.rollno=1
s=Student()                     # object create  got where constrcutor 
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
s1=Student()
print("my name=",s1.name)
print("my rollno=",s1.rollno)
print("clg name=",s1.clg)

