def check(no):
	if no %2==0:
		return True
	else:
		return False
print("enter a number")
no=int(input())
if check(no):
	print("even no")
else:
	print("odd no")