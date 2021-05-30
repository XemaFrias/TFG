import pandas as pd
import neurokit2 as nk
from scipy.signal import find_peaks
from scipy import stats
#mport matplotlib.pyplot as plt
import sys
#plt.rcParams['figure.figsize'] = [15, 9]
salida=open("ECG_data.csv","a")
a= "ECGsal_sub_"
b= ".csv"
c=sys.argv[1]
f= a+c+b
output=""
outputComp="ECG_comp_sub"+c
salidaComp=open(outputComp,"w")
data = pd.read_csv(f)
umbral_low=0
umbral_top=5
#Pinemos el umbral maximo en 40 minutos
while umbral_top<2450:
	outputComp=str(umbral_top)+"\n"
	salidaComp.write(outputComp)
	data_segment=data.loc[(data['segs']>=umbral_low) & (data['segs']< umbral_top)]
	#Limpiamos la señal y buscamos los picos directamente
	clean = nk.ecg_clean(data_segment['ecg'], sampling_rate=1000)
	clean=stats.zscore(clean)
	info = nk.ecg_findpeaks(clean)
	#signals, info = nk.ecg_process(data_segment['ecg'], sampling_rate=1000)
	rpeaks = info["ECG_R_Peaks"]
	hrv_indices= nk.hrv_time(rpeaks, sampling_rate=1000, show=False)
	output=""
	output+=(str(umbral_low)+","+str(umbral_top)+",")
	output+=(str(int(data_segment.iloc[0]['video']))+","+str(int(data_segment.iloc[-1]['video']))+",")
	output+=(str(hrv_indices.iloc[0]['HRV_MeanNN'])+","+str(hrv_indices.iloc[0]['HRV_SDNN'])+","+str(hrv_indices.iloc[0]['HRV_pNN20'])+","+str(hrv_indices.iloc[0]['HRV_pNN50'])+"\n")
	salida.write(output)
	umbral_low+=1
	umbral_top+=1
