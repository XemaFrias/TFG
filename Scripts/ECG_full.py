import os
#escribimos cabecera de ecg
salida=open("GSR_data.csv","w")
cabecera="segundo_init,segundo_fin,video_init,video_fin,HRV_MeanNN,HRV_SDNN,HRV_SDNN,HRV_pNN50"
salida.write(cabecera)
salida.close()
salidaECG=open("GSR_Comp.csv","w")
for x in range(1,31):
	print(x)
	output="Prueba" +str(x)+"\n"
	cmd="python3 GSR.py "+ str(x)
	os.system(cmd)	
	salidaECG.write(output)