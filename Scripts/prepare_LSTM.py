from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
 
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	print(df)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

#PRIMERA SECCIÓN: PREPARAR EL DATASET 
# load dataset
dataset = read_csv('Dataset.csv')
values = dataset.pop('feeling').values
# integer encode direction
encoder = LabelEncoder()
values = encoder.fit_transform(values)
# ensure all data is float
values = values.astype('float32')
# normalize features
#scaler = MinMaxScaler(feature_range=(0, 1))
#scaled = scaler.fit_transform(values)
# frame as supervised learning
dataset['feeling']=values
print(dataset)
#Usaremos 5 medidas a pasado para intentar ver una a futuro
reframed = series_to_supervised(dataset, 5, 1)
# drop columns we don't want to predict
for x in range (21,34):
	reframed.drop(reframed.columns[x], axis=1, inplace=True)
reframed.to_csv(r'LSTM_Dataframe.csv')	
salida=open("log.txt","w")
output=""
output=reframed.head().to_string()
salida.write(output)