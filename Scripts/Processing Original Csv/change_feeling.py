
for x in range(1,31):
	#Prperar el nombre de los archivos y abrir
	a= "sub_"
	b= ".csv"
	c=str(x)
	f= a+c+b
	file = open(f)
	sal ="sal_"+a+c+b
	salida = open(sal,"w")
	line= file.readline()
	salida.write(line)
	line= file.readline().strip("\n").split(",")
	output=""
	while len(line)>1:
		#Copiar las lineas cambiando la posicion final
		if line[9] == "1":
			line[9] = "1"
		elif line[9] == "2":
			line[9] = "1"
		elif line[9] == "3":
			line[9] = "2"
		elif line[9] == "4":
			line[9] = "2"
		elif line[9] == "5":
			line[9] = "3"
		elif line[9] == "6":
			line[9] = "3"
		elif line[9] == "7":
			line[9] = "4"
		elif line[9] == "8":
			line[9] = "4"
		elif line[9] == "9":
			line[9] = "0"
		elif line[9] == "10":
			line[9] = "0"
		elif line[9] == "11":
			line[9] = "0"
		elif line[9] == "12":
			line[9] = "0"				
		output= ','.join(line)
		output += "\n"	
		salida.write(output)
		line= file.readline().strip("\n").split(",")
	file.close()
	salida.close()
