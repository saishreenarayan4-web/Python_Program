class A:
	print("A static block")
	def __init__(self):
		self.non()
		print("A constructor")
	def non(self):
		print("A non static block")
class B(A):
	print("B static block")
	def __init__(self):
		super().__init__()
		self.non1()
		print("B constructor")
	def non1(self):
		print("B non static block")
ob=B()
obj=B()