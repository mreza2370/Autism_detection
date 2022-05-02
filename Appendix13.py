#==================================================
# Creating our model
import keras
from keras. models import Sequential
from keras. layers import Dense, Dropout,Flatten,Conv2D,MaxPool2D
from keras. optimizers import SGD
from keras. losses import categorical_crossentropy
from keras. layers import BatchNormalization
from keras. utils import plot_model

myModel = Sequential()

myModel. add(Conv2D(16, 2, activation='selu', padding='same', strides=1,input_shape=(10,10,1)))
myModel. add(Conv2D(64, 2, activation='selu', padding='same', strides=1))
myModel. add(Conv2D(64, 2, activation='selu', padding='same', strides=1))
myModel. add(MaxPool2D(pool_size=1,strides=None,padding='same'))
myModel. add(Conv2D(80, 2, activation='selu', padding='same', strides=1))
myModel. add(Conv2D(80, 2, activation='selu', padding='same', strides=1))
myModel. add(MaxPool2D(pool_size=1,strides=None,padding='same'))
myModel. add(Conv2D(80, 2, activation='selu', padding='same', strides=1))

myModel. add(Flatten())

myModel. add(Dense(90, activation='relu'))
myModel. add(Dropout(20))
myModel. add(BatchNormalization())
myModel. add(Dense(90, activation='relu'))
myModel. add(Dropout(20))
myModel. add(BatchNormalization())
myModel. add(Dense(90, activation='relu'))
myModel. add(Dropout(20))
myModel. add(BatchNormalization())
myModel. add(Dense(50, activation='relu'))
myModel. add(Dropout(20))
myModel. add(BatchNormalization())
myModel. add(Dense(25, activation='relu'))
myModel. add(Dropout(20))
myModel. add(BatchNormalization())
myModel. add(Dense(5, activation='softmax'))
myModel. add(Dense(5, activation='softmax'))

myModel. summary()
plot_model(myModel, to_file='model1. png')
myModel. compile(optimizer=keras. optimizers. Nadam(lr=0. 001), loss='binary_crossentropy', metrics=['accuracy'])

#==================================================
# Train our model
myModel. fit(data_final, lebel_ex, batch_size=500, epochs=600, validation_split=0. 2)
