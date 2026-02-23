class Employe:
	def __init__(self,Id,name,sal):
		self.Id=Id
		self.name=name
		self.sal=sal
		
	def show(self):
		print("Employe Id=",self.Id)
		print("Employe name=",self.name)
		print("salary of Employe=",self.sal)
#a=employe()
print("enter Employe Id")
Id=int(input())
print("enter Employe name")
name=str(input())
print("enter salary of Employe")
sal=float(input())
d=Employe(Id,name,sal)
d.show()
		