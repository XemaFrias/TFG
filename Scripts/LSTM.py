from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
 
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
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
values=dataset.values
#Usaremos 5 medidas a pasado para intentar ver una a futuro
# specify the number of lag hours
n_segundos = 5
n_features = 14
reframed = series_to_supervised(values, n_segundos, 1)
# drop columns we don't want to predict
reframed.drop(['var1(t)','var2(t)','var3(t)','var4(t)','var5(t)','var6(t)','var7(t)','var8(t)','var9(t)','var10(t)','var11(t)','var12(t)','var13(t)'],axis=1,inplace=True)
#Los siguiente era para depurar que lo anterior saliese bien
#reframed.to_csv(r'export_dataframe.csv')	
salida=open("log.txt","w")
output=""
output=reframed.head().to_string()
salida.write(output)

#SEGUNDA PARTE: PREPARAR PARA INTRODUCIR AL LSTM
# split into train and test sets
values = reframed.values
n_entradas_Train = 365 * 24
train = values[:n_entradas_Train, :]
test = values[n_entradas_Train:, :]
# split into input and outputs
n_obs = n_segundos * n_features
train_X, train_y = train[:, :n_obs], train[:, -n_features]
test_X, test_y = test[:, :n_obs], test[:, -n_features]
print(train_X.shape, len(train_X), train_y.shape)
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], n_segundos, n_features))
test_X = test_X.reshape((test_X.shape[0], n_segundos, n_features))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)


# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()
