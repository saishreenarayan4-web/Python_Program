def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=facttest(3)+facttest(4)+facttest(5)
print("factorial sum=",s)