class Mycomplex:
	def __init__(self,r,i):
		self.__r=r
		self.__i=i
	def show(self):
		print(self._r,"+",self._i,"i")
c1=Mycomplex(2,3)
c2=Mycomplex(3,4)
c3=Mycomplex(0,0)
#c3=c1+c2  error
c3._r=c1_.r+c2._r 
c3._i=c1_.i+c2._i  
c1.show()
c2.show()
c3.show()