r = int(input('enter the no.of rows : '))
c = int(input('enter the no.of coloums : '))


a = []

n = 0

for i in range(0,r):
	tempList = []
	for j in range(0,c):
		tempList.append(0)
	a.append(tempList)


if r > c:
	for i in range(0,c):
		tempNum1 = -1
		for j in range(i,-1,-1):
			tempNum1+=1
			n += 1
			a[j][tempNum1] = n

	for i in range(0,c):
		tempNum2 = r
		for j in range(i,c):
			tempNum2-=1
			n += 1
			a[tempNum2][j] = n

else:
	for i in range(0,r):
		tempNum3 = -1
		for j in range(i,-1,-1):
			tempNum3+=1
			n += 1
			a[j][tempNum3] = n

	for i in range(1,c):
		tempNum4 = r
		for j in range(i,c):
			tempNum4-=1
			n += 1
			a[tempNum4][j] = n

print('\n')
for i in range(0,r):
	tempStr = ''
	for j in range(0,c):
		tempStr = tempStr + str(a[i][j]) + '\t'
	print(tempStr)
