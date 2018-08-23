def Let_Review(list):
	
	
	for item in list:
		str_even=""
		str_odd=""
		count=0
		for char in item:
			if count % 2==0:
				str_even+=char
			else:str_odd+=char
			count+=1
		print str_even + " " +  str_odd


nos=raw_input()
list=[]
for x in range(0,int(nos)):
	str=raw_input()
	list.append(str)
	
Let_Review(list)



