# Creating our model (FC)
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.losses import categorical_crossentropy
from keras.layers import BatchNormalization

myModel = Sequential()
myModel.add(Dense(90, activation='relu', input_shape=(100,)))
myModel.add(Dropout(20))
myModel.add(Dense(90, activation='relu'))
myModel.add(Dropout(20))
myModel.add(Dense(90, activation='relu'))
myModel.add(BatchNormalization())
myModel.add(Dense(50, activation='relu'))
myModel.add(Dropout(20))
myModel.add(Dense(25, activation='relu'))
myModel.add(BatchNormalization())
myModel.add(Dense(5, activation='softmax'))
myModel.add(Dense(5, activation='softmax'))

from keras.utils import plot_model
plot_model(myModel, to_file='model.png',show_shapes=True,show_layer_names=True,expand_nested =True,rankdir)

myModel.summary()
myModel.compile(optimizer='Nadam', loss='binary_crossentropy', metrics=['accuracy'])
myModel.fit(data_final,lebel_ex, epochs=600,shuffle=True,batch_size=500, validation_split=0.2)
