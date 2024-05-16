import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split as tts 
from keras.layers import Dense , Input , Dropout
from keras.models import Model
np.random.seed(42)

data = pd.read_excel('/content/Real estate valuation data set.xlsx')
data=data.dropna()#delets the null elements

#input and output
x=data.drop('Y house price of unit area', axis = 1)
y=data['Y house price of unit area'].values
xs=scale(x)

print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
#reshapeing
x_train=x_train.reshape(-1,7,1)#-1 : we put it except of puting 717 for example
x_test=x_test.reshape(-1,7,1)# 1 : is for dimensions (for video or pic)

#here we use with no deepness cause we do not need more 

inputs=Input(shape=(7,))#input layer
x= inputs
x= Dense(256,activation='relu')(x)#1st hidden layer (number_of_perceptrons,activation_function)
x= Dense(512,activation='relu')(x)#2nd layer
x= Dense(1024,activation='relu')(x)#3rd layer
x= Dense(2048,activation='relu')(x)#4th layer
x= Dense(4096,activation='relu')(x)#5th layer
x= Dense(8129,activation='relu')(x)#6th layer
x= Dense(4096,activation='relu')(x)#7th layer
x= Dense(2048,activation='relu')(x)#8th layer
x= Dense(1024,activation='relu')(x)#9th layer
x= Dense(512,activation='relu')(x)#10th layer
x= Dense(256,activation='relu')(x)#11th layer
output=Dense(1,activation='linear')(x)#output layer 
model=Model(inputs,output)

model.compile(optimizer='rmsprop',loss='mse')
model.fit(x_train,y_train,batch_size=1000, epochs=200)

loss=model.evaluate(x_test,y_test,batch_size=10)
loss=model.evaluate(x_train,y_train,batch_size=10)
ypred=model.predict(x_test)
ypred=ypred.reshape(-1,)

xx=[0,80]
plt.scatter(y_test,ypred)
plt.plot(xx,xx,'r--')
plt.xlabel('predict')
plt.ylabel('real')
plt.show()