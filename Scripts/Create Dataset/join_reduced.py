fileECG=open("ECG_data.csv")
fileGSR=open("GSR_data.csv")
fileTemp=open("Temp_data.csv")
lineECG= fileECG.readline().strip("\n").split(",") #hasta 7
lineGSR= fileGSR.readline().strip("\n").split(",") #hasta 8
lineTemp= fileTemp.readline().strip("\n").split(",") #hasta 5
salida=open("Dataset_2_reduced.csv","w")
salida.write("paciente,segundo_init,segundo_fin,HRV_MeanNN,HRV_SDNN,HRV_pNN20,HRV_pNN50,GSR_MEAN,GSR_STD,GSR_MAX,GSR_MIN,GSR_RANGE,Temp_MEAN,Temp_STD,feeling\n")
paciente=1
aux=0
while(lineECG[0]!=""):
	lineECG= fileECG.readline().strip("\n").split(",") 
	lineGSR= fileGSR.readline().strip("\n").split(",")
	lineTemp= fileTemp.readline().strip("\n").split(",") 
	print(lineECG[0])
	if(int(lineECG[0])<aux):
		paciente+=1
	aux=int(lineECG[0])	
	#Temp tiene el mismo numero de instancias que GSr por lo que no hace falta comprobar
	while (int(lineECG[0])<int(lineGSR[0])):
		#algunas lineas de ecg no pudieron procesarse por lo que avanzamos hasta el siguiente GSR
		lineGSR= fileGSR.readline().strip("\n").split(",")
		lineTemp= fileTemp.readline().strip("\n").split(",") 
	if (lineECG[0]==lineGSR[0]):
		output=""
		#escribimos los features extraidos
		output+=str(paciente)+","
		output+=lineECG[0]+","+lineECG[1]+","
		output+=lineECG[4]+","+lineECG[5]+","+lineECG[6]+","+lineECG[7]+","
		output+=lineGSR[4]+","+lineGSR[5]+","+lineGSR[6]+","+lineGSR[7]+","+lineGSR[8]+","
		output+=lineTemp[4]+","+lineTemp[5]+","
		#modificamos el vector de salida

		video="" #neutral,amusing,boring,relaxing,scary,direction(if 0, left to right)
		if (lineECG[2]=="0" ):
			video="neutral"
		if (lineECG[2]=="1"):
			video="amusing"
		if (lineECG[2]=="2" ):
			video="boring"
		if (lineECG[2]=="3" ):
			video="relaxing"
		if (lineECG[2]=="4" ):
			video="scary"
		output+=video+"\n"					
		salida.write(output)
		