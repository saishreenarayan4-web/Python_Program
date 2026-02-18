L1=[[1,2,3],[4,5,6]]
L2=[[2,5,1],[3,4,2]]
L3=[]
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		x.append(L1[i][j]+L2[i][j])
	L3.append(x)
print(L3)




'''L1=[[1,2,3],[4,5,6]]
L2=[[2,5,1],[3,4,2]]
L3=[[L1[i][j]+L2[i][j] for j in range(len(L1[i]))] for i in range(len(L1))]
print(L3)