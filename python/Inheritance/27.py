class A:
	print("A static block")
	def __init__(self):
		print("A constructor")
class B(A):
	print("B static block")
	def __init__(self):
		super().__init__()
		print("B constructor")
ob=B()
obj=B()