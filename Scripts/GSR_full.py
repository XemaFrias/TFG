import os
#escribimos cabecera de ecg
salida=open("ECG_data.csv","w")
cabecera="segundo_init,segundo_fin,video_init,video_fin,HRV_MeanNN,HRV_SDNN,HRV_SDNN,HRV_pNN50"
salida.write(cabecera)
salida.close()
#escribimos cabecera de GSR
salida=open("GSR_data.csv","w")
cabecera="segundo_init,segundo_fin,video_init,video_fin,GSR_MEAN,GSR_STD,GSR_MAX,GSR_MIN,GSR_RANGE"
salida.write(cabecera)
salida.close()
#escribimos cabecera de Temperatura
salida=open("Temp_data.csv","w")
cabecera="segundo_init,segundo_fin,video_init,video_fin,TEMP_MEAN,TEMP_STD"
salida.write(cabecera)
salida.close()
#Preparamos csv para comprobaciones
salida=open("GSR_Comp.csv","w")
salidaECG=open("ECG_Comp.csv","w")
salidaTEMP=open("TEMP_Comp.csv","w")
for x in range(1,31):
#	print(x)
	output="Prueba" +str(x)+"\n"
	cmd="python3 GSR.py "+ str(x)
	os.system(cmd)
	salida.write(output)
print("Empezamos ECG")	
for x in range(1,31):
	output="Prueba" +str(x)+"\n"
	cmd="python3 ECG.py "+ str(x)
	os.system(cmd)	
	salidaECG.write(output)
print("Empezamos TEMP")	
for x in range(1,31):
	output="Prueba" +str(x)+"\n"
	cmd="python3 Temp.py "+ str(x)
	os.system(cmd)	
	salidaECG.write(output)	