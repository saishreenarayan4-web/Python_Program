def si():
	print("enter princle,rate of intrest,time")
	p=float(input("enter principle amount"))
	r=float(input("enter rate of intrest"))
	t=float(input("enter time in year"))
	si=(p*t*r)/100
	print("principle amount=",p)
	print("rate of intrest=",r)
	print("time in year=",t)
	print("simple intrest=",si)
	return
si()