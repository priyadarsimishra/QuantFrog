from tensorflow.keras.models import load_model
import tensorflow as tf
import pandas as pd
from webcrawler import get_dataset
from sklearn.preprocessing import MinMaxScaler

ticker = "AMZN"

model = tf.keras.models.load_model("earningforcaster.h5")
print(model.summary())

data = get_dataset()
quarters = 12
points = []
for val, row in data.iterrows():
    if row['ticker'] == ticker:
        points.append(float(row['eps-earnings-per-share-diluted']))

points = pd.DataFrame(points[len(points) - quarters:])
print(points.shape)

scaler = MinMaxScaler()
prediction = model.predict(points)
scaler.fit(points)
# for pred in prediction:
pred1 = scaler.inverse_transform(prediction)[0][0]
pred2 = scaler.inverse_transform(prediction)[1][0]
print(pred1, pred2)
# print(prediction)
# for 