class A:
	print("A static block")
	def __init__(self):
		print("A constructor")
class B(A):
	pass
ob=B()