import numpy
sal="salida.csv"
salida = open(sal,"a")
for x in range(1,31):
	#Prperar el nombre de los archivos y abrir
	print(x)
	a= "anno_sub_"
	b= ".csv"
	c=str(x)
	f= a+c+b
	file = open(f)
	line= file.readline()
	#Leemos dos veces para ignorar la instancia con el nombre de las columnas
	line= file.readline().strip("\n").split(",")
	output=""
	segundo=0
	video=0
	acumuladoVal=[]
	acumuladoArous=[]
	video="0"
	while len(line)>1:
		lineaux=list(line)
		if line[0]!=str(segundo):
			#Cuando cambia de segundo, calculamos la media para ese segundo
			acumuladoVal.sort()
			acumuladoArous.sort()
			lineaux[1]=str(numpy.mean(acumuladoVal))
			lineaux[2]=str(numpy.mean(acumuladoArous))
			lineaux.append(str(numpy.median(acumuladoVal)))
			lineaux.append(str(numpy.std(acumuladoVal)))
			lineaux.append(str(numpy.var(acumuladoVal)))

			lineaux.append(str(numpy.median(acumuladoArous)))
			lineaux.append(str(numpy.std(acumuladoArous)))
			lineaux.append(str(numpy.var(acumuladoArous)))

			acumuladoArous[:] = []
			acumuladoVal[:] = []
			segundo+=1	
			output= ','.join(lineaux)
			output += "\n"	
			salida.write(output)		

		elif line[3]!= video:
			#Cuando se produce un cambio de video en el mismo segundo, calculamos tambien la media para ese intervalo para evitar datos erroneos
			acumuladoVal.sort()
			acumuladoArous.sort()
			lineaux[1]=str(numpy.mean(acumuladoVal))
			lineaux[2]=str(numpy.mean(acumuladoArous))
			lineaux.append(str(numpy.median(acumuladoVal)))
			lineaux.append(str(numpy.std(acumuladoVal)))
			lineaux.append(str(numpy.var(acumuladoVal)))

			lineaux.append(str(numpy.median(acumuladoArous)))
			lineaux.append(str(numpy.std(acumuladoArous)))
			lineaux.append(str(numpy.var(acumuladoArous)))

			acumuladoArous[:] = []
			acumuladoVal[:] = []
			video=line[3]	
			output= ','.join(lineaux)
			output += "\n"	
			salida.write(output)	

		#Esto se repite siempre ya sea para avanzar en ese segunfo o para escribir bien lo que aparezca en ese segundo
		acumuladoVal.append(float(line[1]))
		acumuladoArous.append(float(line[2]))
		line= file.readline().strip("\n").split(",")
	#Al terminar, recogemos tambien los datos del ultimo segundo antes de volvera empezar el loop
	acumuladoVal.sort()
	acumuladoArous.sort()
	lineaux[1]=str(numpy.mean(acumuladoVal))
	lineaux[2]=str(numpy.mean(acumuladoArous))
	lineaux.append(str(numpy.median(acumuladoVal)))
	lineaux.append(str(numpy.std(acumuladoVal)))
	lineaux.append(str(numpy.var(acumuladoVal)))

	lineaux.append(str(numpy.median(acumuladoArous)))
	lineaux.append(str(numpy.std(acumuladoArous)))
	lineaux.append(str(numpy.var(acumuladoArous)))	
	output= ','.join(lineaux)
	output += "\n"	
	salida.write(output)
	file.close()
salida.close()
