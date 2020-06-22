
def stl_num(index=0):
	listnum = []
	for i in range(10):
		for j in range(10):
			for k in range(10):
				num = (f'{i}{j}{k}')
				listnum.append(num)
	print(listnum)
	return listnum[index]

print(stl_num(10))
