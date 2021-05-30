file=open("Dataset_2.csv")
line= file.readline().strip("\n").split(",")
aux=0
counter=1
while (line[0]!=""):
	line= file.readline().strip("\n").split(",")
	if (int(line[0])>aux):
		aux=(int(line[0]))
	else:
		counter+=1
		print(aux)
		print(counter)
		aux=(int(line[0]))	
print(counter)		
