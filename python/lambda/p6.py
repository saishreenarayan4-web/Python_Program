def si(p,r,t):
	s=(p*t*r)
	return s
p=float(input("enter priciple amount"))
r=float(input("enter  rate"))
t=float(input("enter time in year"))
res=si(p,r,t)
print("simple intresrt=",res)