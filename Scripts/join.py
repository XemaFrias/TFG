fileECG=open("ECG_data.csv")
fileGSR=open("GSR_data.csv")
fileTemp=open("Temp_data.csv")
lineECG= fileECG.readline().strip("\n").split(",") #hasta 7
lineGSR= fileGSR.readline().strip("\n").split(",") #hasta 8
lineTemp= fileTemp.readline().strip("\n").split(",") #hasta 5
salida=open("Dataset_2.csv","w")
salida.write("segundo_init,segundo_fin,HRV_MeanNN,HRV_SDNN,HRV_pNN20,HRV_pNN50,GSR_MEAN,GSR_STD,GSR_MAX,GSR_MIN,GSR_RANGE,Temp_MEAN,Temp_STD,feeling\n")
while(lineECG[0]!=""):
	lineECG= fileECG.readline().strip("\n").split(",") 
	lineGSR= fileGSR.readline().strip("\n").split(",")
	lineTemp= fileTemp.readline().strip("\n").split(",") 
	print(lineECG[0])
	#Temp tiene el mismo numero de instancias que GSr por lo que no hace falta comprobar
	while (int(lineECG[0])<int(lineGSR[0])):
		#algunas lineas de ecg no pudieron procesarse por lo que avanzamos hasta el siguiente GSR
		lineGSR= fileGSR.readline().strip("\n").split(",")
		lineTemp= fileTemp.readline().strip("\n").split(",") 
	if (lineECG[0]==lineGSR[0]):
		output=""
		#escribimos los features extraidos
		output+=lineECG[0]+","+lineECG[1]+","
		output+=lineECG[4]+","+lineECG[5]+","+lineECG[6]+","+lineECG[7]+","
		output+=lineGSR[4]+","+lineGSR[5]+","+lineGSR[6]+","+lineGSR[7]+","+lineGSR[8]+","
		output+=lineTemp[4]+","+lineTemp[5]+","
		#modificamos el vector de salida
		video=[0,0,0,0,0,0] #neutral,amusing,boring,relaxing,scary,direction(if 0, left to right)
		if (lineECG[2]=="0" or lineECG[3]=="0"):
			video[0]=1
		if (lineECG[2]=="1" or lineECG[3]=="1"):
			video[1]=1
		if (lineECG[2]=="2" or lineECG[3]=="2"):
			video[2]=1
		if (lineECG[2]=="3" or lineECG[3]=="3"):
			video[3]=1
		if (lineECG[2]=="4" or lineECG[3]=="4"):
			video[4]=1
		#Miramos si el primer video es mayor que el segundo y si lo es tenemos que marcar que la dirección es a la izquierda	
		if (int(lineECG[2])>int(lineECG[3])):
			video[5]=1	
		output+="\""+ str(video)+"\""  +"\n"					
		salida.write(output)
		