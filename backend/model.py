from webcrawler import get_dataset
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.models import save_model
from collections import deque
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt



df = get_dataset()
df.index = df["date"]
df.drop("date", axis=1, inplace=True)
df.drop("ticker", axis=1, inplace=True)
print(df)

LOOKUP_STEPS = [1, 2]
N_STEPS = 12 # we want quarterly

def GetTrainedModel(x_train, y_train):
    model = Sequential()
    model.add(LSTM(60, return_sequences=True, input_shape=(N_STEPS, len(['eps-earnings-per-share-diluted']))))
    model.add(Dropout(0.3))
    model.add(LSTM(120, return_sequences=False))
    model.add(Dropout(0.3))
    model.add(Dense(20))
    model.add(Dense(1))

    BATCH_SIZE = 8
    EPOCHS = 20

    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(x_train, y_train,
                validation_split=0.33,
                batch_size=BATCH_SIZE,
                epochs=EPOCHS,
                verbose=1)
    
    model.save("earningforcaster.h5")
    model.summary()


    return model

scaler = MinMaxScaler()
print(df.columns)
# print(df['revenue'].values)
df['revenue'] = scaler.fit_transform(np.expand_dims(df['revenue'].values, axis=1))
df['ebit'] = scaler.fit_transform(np.expand_dims(df['ebit'].values, axis=1))
df['cash-flow-from-operating-activities'] = scaler.fit_transform(np.expand_dims(df['cash-flow-from-operating-activities'].values, axis=1))
df['current-ratio'] = scaler.fit_transform(np.expand_dims(df['current-ratio'].values, axis=1))
df['debt-equity-ratio'] = scaler.fit_transform(np.expand_dims(df['debt-equity-ratio'].values, axis=1))
df['gross-margin'] = scaler.fit_transform(np.expand_dims(df['gross-margin'].values, axis=1))
df['net-profit-margin'] = scaler.fit_transform(np.expand_dims(df['net-profit-margin'].values, axis=1))
df['roe'] = scaler.fit_transform(np.expand_dims(df['roe'].values, axis=1))
# df['ebitda-margin'] = scaler.fit_transform(np.expand_dims(df['ebitda-margin'].values, axis=1))
df['past-eps-earnings-per-share-diluted'] = scaler.fit_transform(np.expand_dims(df['past-eps-earnings-per-share-diluted'].values, axis=1))
df['eps-earnings-per-share-diluted'] = scaler.fit_transform(np.expand_dims(df['eps-earnings-per-share-diluted'].values, axis=1))

def PrepareData(quarters):
  dataframe = df.copy()
  dataframe['future'] = dataframe['eps-earnings-per-share-diluted'].shift(-quarters)
  last_sequence = np.array(dataframe[['eps-earnings-per-share-diluted']].tail(quarters))
  dataframe.dropna(inplace=True)
  sequence_data = []
  sequences = deque(maxlen=N_STEPS)

  for entry, target in zip(dataframe[['eps-earnings-per-share-diluted']].values, dataframe['future'].values):
      sequences.append(entry)
      if len(sequences) == N_STEPS:
          sequence_data.append([np.array(sequences), target])

  last_sequence = list([s[:len(['eps-earnings-per-share-diluted'])] for s in sequences]) + list(last_sequence)
  last_sequence = np.array(last_sequence).astype(np.float32)

  # construct the X's and Y's
  X, Y = [], []
  for seq, target in sequence_data:
      X.append(seq)
      Y.append(target)

  # convert to numpy arrays
  X = np.array(X)
  Y = np.array(Y)

  return dataframe, last_sequence, X, Y

predictions = []

for step in LOOKUP_STEPS:
  df, last_sequence, x_train, y_train = PrepareData(step)
  x_train = x_train[:, :, :len(['eps-earnings-per-share-diluted'])].astype(np.float32)

  model = GetTrainedModel(x_train, y_train)

  last_sequence = last_sequence[-N_STEPS:]
  last_sequence = np.expand_dims(last_sequence, axis=0)
  print("last_sequence:", last_sequence)
  prediction = model.predict(last_sequence)
  predicted_price = scaler.inverse_transform(prediction)[0][0]
  print("predicted price:", predicted_price)

  predictions.append(round(float(predicted_price), 2))

# df = scaler.inverse_transform(df)
inverse_scaled = scaler.inverse_transform(df[['eps-earnings-per-share-diluted']])
print(inverse_scaled)
print("pred:", predictions)

print(df)