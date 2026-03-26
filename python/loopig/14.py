'''12344321
   123  321
   12    21
   1      1'''
c=0
for i in range(4,0,-1):

	for j in range(1,i+1,1):
		print(j,end="")

	for j in range(0,2*(4-i),1):
		print(end=" ")

	for j in range(i,0,-1):
		print(j,end="")
	c=c+2
	print()
