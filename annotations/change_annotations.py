for x in range(1,31):
	print(x)
	#Prperar el nombre de los archivos y abrir
	a= "sub_"
	b= ".csv"
	c=str(x)
	f= a+c+b
	file = open(f)
	sal ="anno_"+a+c+b
	salida = open(sal,"w")
	line= file.readline()
	salida.write(line)
	line= file.readline().strip("\n").split(",")
	output=""
	while len(line)>1:
		line[0]= str(int(line[0])/1000)
		#Copiar las lineas cambiando la posicion final
		if line[3] == "1":
			line[3] = "1"
		elif line[3] == "2":
			line[3] = "1"
		elif line[3] == "3":
			line[3] = "2"
		elif line[3] == "4":
			line[3] = "2"
		elif line[3] == "5":
			line[3] = "3"
		elif line[3] == "6":
			line[3] = "3"
		elif line[3] == "7":
			line[3] = "4"
		elif line[3] == "8":
			line[3] = "4"
		elif line[3] == "9":
			line[3] = "0"
		elif line[3] == "10":
			line[3] = "0"
		elif line[3] == "11":
			line[3] = "0"
		elif line[3] == "12":
			line[3] = "0"				
		output= ','.join(line)
		output += "\n"	
		salida.write(output)
		line= file.readline().strip("\n").split(",")
	file.close()
	salida.close()
