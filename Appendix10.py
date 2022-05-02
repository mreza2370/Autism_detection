
#==================================================
# Creating our model
from keras. models import Model
from keras import layers
import keras
myInput=layers. Input(shape=(10,10,1))
conv1 = layers. Conv2D(16, 3, activation='selu', padding='same', strides=2)(myInput)
conv2 = layers. Conv2D(32, 3, activation='selu', padding='same', strides=2)(conv1)
flat = layers. Flatten()(conv2)
out_layer = layers. Dense(5, activation='softmax')(flat)

myModel = Model(myInput, out_layer)

myModel. summary()
myModel. compile(optimizer=keras. optimizers. Nadam(), loss=keras. losses. binary_crossentropy, metrics=['accuracy'])

#==================================================
# Train our model
myModel. fit(data_final, lebel_ex, batch_size=500, epochs=300, validation_split=0. 2)
