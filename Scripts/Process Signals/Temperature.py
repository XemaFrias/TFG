import pandas as pd
import numpy as np
import sys
#plt.rcParams['figure.figsize'] = [15, 9]
salida=open("Temp_data.csv","a")

a= "Temp_sal_sub_"
b= ".csv"
c=sys.argv[1]
f= a+c+b
outputComp="Temp_comp_sub"+c
salidaComp=open(outputComp,"w")
data = pd.read_csv(f)
#Definir los límites de la ventana
umbral_low=0
umbral_top=5
#Pinemos el umbral maximo en 40 minutos
while umbral_top<2450:
	outputComp=str(umbral_top)+"\n"
	salidaComp.write(outputComp)
	#Obtener los datos para esta ventana
	data_segment=data.loc[(data['segs']>=umbral_low) & (data['segs']< umbral_top)]
	clean = pd.DataFrame(data_segment['skt']).to_numpy()
	media=np.mean(clean)
	std=np.std(clean)
	output=""
	output+=(str(umbral_low)+","+str(umbral_top)+",")
	output+=(str(int(data_segment.iloc[0]['video']))+","+str(int(data_segment.iloc[-1]['video']))+",")
	output+=(str(media)+","+str(std)+"\n")
	salida.write(output)
	print(umbral_top)

	umbral_low+=1
	umbral_top+=1
