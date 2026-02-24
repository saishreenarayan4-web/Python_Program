class Test:
	def __init__(self):
		self.a=10
		self.__b=20
t=Test()
print(t.a)  #10
#print(t.__b)  error

