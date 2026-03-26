class shape:
	def area(self):
		print("area method from shape")

class rectangle(shape):
	def __init__(self,lenghth,bradth):
		self.lenghth = lenghth
		self.breadth = breadth

	def area(self):
		print("area of rectangle",self.lenghth * self.breadth)
		