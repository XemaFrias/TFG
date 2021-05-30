import numpy
for x in range(1,31):
	#Prperar el nombre de los archivos y abrir
	print(x)
	a= "sal_sub_"
	b= ".csv"
	c=str(x)
	f= a+c+b
	file = open(f)
	line= file.readline().strip("\n").split(",")
	salECG ="ECG"+a+c+b
	salidaECG = open(salECG,"w")
	salGSR ="GSR"+a+c+b
	salidaGSR = open(salGSR,"w")
	outputGSR= line[0]+",segs,"+line[3]+ ","+ line[9]+"\n"
	salidaGSR.write(outputGSR)
	outputECG= line[0]+",segs,"+line[1]+ ","+ line[9]+"\n"
	salidaECG.write(outputECG)
	#Leemos dos veces para ignorar la instancia con el nombre de las columnas
	line= file.readline().strip("\n").split(",")
	output=""
	while len(line)>1:
		segs=str(int((int (line[0]))/1000)) #usamos doble int para quitar los decimales
		outputGSR= line[0]+","+segs+","+line[3]+ ","+ line[9]+"\n"
		salidaGSR.write(outputGSR)
		outputECG= line[0]+","+segs+","+line[1]+ ","+ line[9]+"\n"
		salidaECG.write(outputECG)
		line= file.readline().strip("\n").split(",")
	file.close()
	salidaECG.close()
	salidaGSR.close()
