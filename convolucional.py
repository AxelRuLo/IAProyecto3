import numpy as np
import tensorflow as tf

import os
from sklearn.model_selection import train_test_split
import keras
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU



def convolucionar(images,directories,dircount):
    labels=[]
    indice=0
    for cantidad in dircount:
        for i in range(cantidad):
            labels.append(indice)
        indice=indice+1

    print("Cantidad etiquetas creadas: ",len(labels))


    deportes=[]
    indice=0
    for directorio in directories:
        name = directorio.split(os.sep)
        print(indice , name[len(name)-1])
        deportes.append(name[len(name)-1])
        indice=indice+1

    print("\n")
    print(f"deportes {deportes}")

    y = np.array(labels)
    X = np.array(images, dtype=np.uint8) 

    
    classes = np.unique(y)
    nClasses = len(classes)
    print('numero de clases : ', nClasses)
    print('clases: ', classes)


    
    train_X,test_X,train_Y,test_Y = train_test_split(X,y,test_size=0.1)
    
    train_X = train_X.astype('float32')
    test_X = test_X.astype('float32')

    train_X = train_X / 255.
    test_X = test_X / 255.
    
    
    train_Y_one_hot = to_categorical(train_Y)
    test_Y_one_hot = to_categorical(test_Y)

    print("\n")
    print(f"conversion x a categorical: {train_Y_one_hot.shape}")
    print(f"conversion y a categorical: {test_Y_one_hot.shape}")
    
    
    print('original y:', train_Y[0])
    print('conversion y:', train_Y_one_hot[0])
    
    train_X,valid_X,train_label,valid_label = train_test_split(train_X, train_Y_one_hot, test_size=0.2, random_state=13)
    
    print(train_X.shape,valid_X.shape,train_label.shape,valid_label.shape)



    INIT_LR = 1e-3
    epochs = 10
    batch_size = 64
    
    print("\n")
    print(f"valores finales")
    print(f"{train_X.shape}")
    print(f"{train_label.shape}")
    print(f"{valid_X.shape}")
    print(f"{valid_label.shape}")

    sport_model = Sequential()
    sport_model.add(Conv2D(64, kernel_size=(7, 7),activation='linear',padding='same',input_shape=(21,28,3)))
    sport_model.add(LeakyReLU(alpha=0.1))
    sport_model.add(MaxPooling2D((2, 2),padding='same'))
    sport_model.add(Dropout(0.5))
    sport_model.add(Flatten())
    sport_model.add(Dense(32, activation='linear'))
    sport_model.add(LeakyReLU(alpha=0.1))
    sport_model.add(Dropout(0.5)) 
    sport_model.add(Dense(nClasses, activation='softmax'))
    
    sport_model.summary()
    
    sport_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=tf.keras.optimizers.Adagrad(lr=INIT_LR, epsilon=None, decay=INIT_LR / 100),metrics=['accuracy'])
    
    sport_train_dropout = sport_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

    test_eval = sport_model.evaluate(test_X, test_Y_one_hot, verbose=1)
    
    
    print('Test loss:', test_eval[0])
    print('Test accuracy:', test_eval[1])
    
    return sport_train_dropout.history["loss"]

