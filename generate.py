a=input('Enter a number: ')
b=input('Enter a number: ')
c=input('Enter a nymner: ')

num_list = []
num_list.append(a)
num_list.append(b)
num_list.append(c)

for i in range(0 , 3):
	for j in range(0, 3):
		for k in range(0 ,3):
			print(f'{num_list[i]} {num_list[j]} {num_list[k]}')