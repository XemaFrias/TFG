
for x in range(1,31):
	#Prperar el nombre de los archivos y abrir
	a= "sal_sub_"
	b= ".csv"
	c=str(x)
	f= a+c+b
	file = open(f)
	amusing= open("amusing","a")
	boring = open("boring","a")
	relaxing = open("relaxing","a")
	scary = open("scary","a")
	neutral = open("neutral","a")
	line= file.readline().strip("\n").split(",")
	output=""
	while len(line)>1:
		#Copiar las lineas cambiando la posicion final
		if line[9] == "1":
			output= ','.join(line)
			output += "\n"	
			amusing.write(output)
		elif line[9] == "2":
			output= ','.join(line)
			output += "\n"	
			boring.write(output)
		elif line[9] == "3":
			output= ','.join(line)
			output += "\n"	
			relaxing.write(output)
		elif line[9] == "4":
			output= ','.join(line)
			output += "\n"	
			scary.write(output)
		elif line[9] == "0":
			output= ','.join(line)
			output += "\n"	
			neutral.write(output)
		line= file.readline().strip("\n").split(",")
	file.close()
	amusing.close()
	boring.close()
	relaxing.close()
	scary.close()
	neutral.close()