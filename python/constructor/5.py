class Rectangle:
	def __init__(self,L,B):   #constrcutor
		self.length=L
		self.breadth=B
	def show(self):
		print("rectangle lenegth=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r=Rectangle(5,7)
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle(10,20)
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())
