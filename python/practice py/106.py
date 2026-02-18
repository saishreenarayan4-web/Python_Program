def check(no):
	if no %2==0:
		return "evenno"
	else:
		return"oddno"
print("enter a number")
no=int(input())
print(check(no))