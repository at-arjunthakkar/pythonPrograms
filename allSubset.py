a = list(range(1,5))
print(a)

subsetCounter = 0
size = 1

x = [[]]

y = []

x.append(y)

while size<=len(a):
	if size == 1:
		subsetCounter+=1
		tempList = []
		tempList.append(a[size-1])
		x.append(tempList)
	if size>1:
		for k in x[1:]:
			ele = k.copy()
			if a[size-1] not in ele:
				ele.append(a[size-1])
				x.append(ele)
				subsetCounter+=1
	size+=1		
			
print(x[1:])

subsetCounter+=1
print("subset count is {} !!".format(subsetCounter))

