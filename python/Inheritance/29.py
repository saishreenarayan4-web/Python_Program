class A:
	print("A static block")
	def __init__(self):
		print("A constructor")
	def __del__(self):
		print("A destructor ")
	
class B(A):
	print("B static block")
	def __init__(self):
		
		print("B constructor")
	def __del__(self):
		print("B destructor ")
	
ob=B()
