L1 = [[1, 2, 3], [4, 5, 6],[7,8,9]]
L3 = []
for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		if i <= j:
			x.append(L1[i][j])
	L3.append(x)
print(L3)







'''L1 = [[1, 2, 3], [4, 5, 6],[7,8,9]]
L3 = [[ L1[i][j] for j in range(len(L1[i])) if i<=j]for i in range(len(L1))]
print(L3)


