import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy import stats
import sys
#plt.rcParams['figure.figsize'] = [15, 9]
#salida=open("GSR_data.csv","a")

a= "GSRsal_sub_"
b= ".csv"
c=sys.argv[1]
f= a+c+b
outputComp="Gsr_comp_sub"+c
salidaComp=open(outputComp,"w")
data = pd.read_csv(f)
#Definir los límites de la ventana
umbral_low=0
umbral_top=5
#Pinemos el umbral maximo en 40 minutos
while umbral_top<2450:
	print(umbral_top)
	outputComp=str(umbral_top)+"\n"
	salidaComp.write(outputComp)
	#Obtener los datos para esta ventana
	data_segment=data.loc[(data['segs']>=umbral_low) & (data['segs']< umbral_top)]
	#aplicar zscore sobre la señal antes de separar
	clean = nk.eda_clean(data_segment['gsr'], sampling_rate=1000)
	clean=stats.zscore(clean)
	phasic=nk.eda_phasic(clean, sampling_rate=1000)
	#Ahora debemos comprobar si la ventana tiene picos o no
	#Hay que pasarlo como lista para evitar problemas con el scipy
	comprobador_picos=list(phasic['EDA_Phasic'].values)
	peaks, _ = find_peaks(comprobador_picos, height=0)
	if len(peaks)>0:
		peaks=nk.eda_findpeaks(phasic, sampling_rate=1000)
		#eda_findpeaks nos da diccionarios por lo que lo transformamos a dataframe para poder hacer el formato bien
		alturas=pd.DataFrame.from_dict(peaks)
		#para poder sacar los features pasamos la columna de las alturas a un array de numpy
		print (alturas)
		alturas_calculos=pd.DataFrame(alturas['SCR_Peaks']).to_numpy()
		#alturas_calculos=pd.DataFrame(signals['SCR_Amplitude']).to_numpy()
		media=np.mean(alturas_calculos)
		std=np.std(alturas_calculos)
		mini=np.amin(alturas_calculos)
		maxi=np.amax(alturas_calculos)
		rang=abs(mini-maxi)
	else:
		media="0"
		std="0"
		mini="0"
		maxi="0"
		rang="0"
	#Por ultimo escribimos el output
	output=""
	output+=(str(umbral_low)+","+str(umbral_top)+",")
	output+=(str(int(data_segment.iloc[0]['video']))+","+str(int(data_segment.iloc[-1]['video']))+",")
	output+=(str(media)+","+str(std)+","+str(maxi)+","+str(mini)+","+str(rang))
	output+="\n"
	#print(output)
	#salida.write(output)

	umbral_low+=1
	umbral_top+=1
