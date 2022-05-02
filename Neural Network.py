import random
import numpy as np
import os
import matplotlib.pyplot as plt
import keras
import csv
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.losses import categorical_crossentropy
import keras.backend as k
from keras.layers import Dropout, Flatten, Dense,Input
from keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle
from keras import optimizers
from keras.callbacks import ModelCheckpoint
from keras.applications.imagenet_utils import preprocess_input



all=[]
train=[]
test=[]
details={1:{'circle':[],'line':[],'square':[]},
         2:{'circle':[],'line':[],'square':[]},
         3:{'circle':[],'line':[],'square':[]},
         4:{'circle':[],'line':[],'square':[]},
         5:{'circle':[],'line':[],'square':[]}}
for r,d,f in os.walk('all'):
    for file in f:
        index=file.index('level')
        level=int(file[index+5])
        level_class='class'+file[index+5]
        all.append([file,level_class])
        if 'circle' in file:
            kind='circle'
        elif 'line' in file:
            kind='line'
        elif 'square' in file:
            kind='square'
        details[level][kind].append([file,level_class])

for level in [1,2,3,4,5]:
    for kind in ['circle','line','square']:
        test.extend(details[level][kind][:100])
        train.extend(details[level][kind][100:])



        
with open('all.csv', newline='',mode='w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['filename','class'])
    for row in all:
        csvwriter.writerow(row)
            
with open('train.csv', newline='',mode='w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['filename','class'])
    for row in train:
        csvwriter.writerow(row)

with open('test.csv', newline='',mode='w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['filename','class'])
    for row in test:
        csvwriter.writerow(row)
        
shape=(480,640,3)
#Here we set the data generators for applying data augmentation methods
train_datagen = ImageDataGenerator(horizontal_flip=True,vertical_flip=True,zoom_range=0.05,rotation_range=360,width_shift_range=0.05,height_shift_range=0.05,shear_range=0.05,preprocessing_function=preprocess_input)
test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
train_df =pd.read_csv('train.csv') #raed train csv file
train_df = shuffle(train_df) #Shuffle the train data
test_df =pd.read_csv('test.csv') #raed train csv file

#Create the generators
train_generator = train_datagen.flow_from_dataframe(
      dataframe=train_df,
      directory='all',
      x_col="filename",
      y_col="class",
      target_size=shape[:2],
      batch_size=30,
      class_mode='categorical',shuffle=True,)

test_generator = test_datagen.flow_from_dataframe(
        dataframe=test_df,
      directory='all',
      x_col="filename",
      y_col="class",
      target_size=shape[:2],
      batch_size=30,
      class_mode='categorical',shuffle=True)

input_tensor=Input(shape=shape)
k.clear_session() #Clear keras backend 
try:
  os.mkdir('models') #create folder for saving the trained networks
except:
  pass
model=keras.applications.MobileNet(input_shape=None,include_top=True,weights=None,input_tensor=input_tensor,classes=5)
model.summary()
model.compile(optimizer=optimizers.Nadam(lr=0.0001), loss='categorical_crossentropy',metrics=['accuracy'])
filepath="models/model-{epoch:02d}-{val_accuracy:.4f}.hdf5" # Path to save the trained models
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', save_best_only=True, mode='max') #creating checkpoint to save the best validation accuracy
callbacks_list = [checkpoint]
model.fit_generator(train_generator, epochs=20,validation_data=test_generator,shuffle=True,callbacks=callbacks_list)
