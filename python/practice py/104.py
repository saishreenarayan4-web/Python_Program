def si():
	si=(p*t*r)/100
	return si
print("enter principle amount")
p=float(input())
print("enter rate of intrest")
r=float(input())
print("enter time in year")
t=float(input())
res=si()
print("simple intrest=",res)