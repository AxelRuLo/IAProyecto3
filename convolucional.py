import numpy as np
import tensorflow as tf
import os
from PIL import Image
from tensorflow import keras



def convolucionar(rutaPrueba:str):
    
    categorias = []
    labels = [];
    imagenes = [];

    categorias = os.listdir("objetos/");

    x= 0
    for directorio in categorias:
        for imagen in os.listdir("objetos/"+directorio):
            img = Image.open("objetos/"+directorio+"/"+imagen).resize((100,100))
            img = np.asarray(img)
            imagenes.append(img)
            labels.append(x)
        x+=1
    imagenes = np.array(imagenes,dtype=np.uint8);

    labels = np.asarray(labels)

    print("\n")

    print(len(labels))
    print(imagenes[0].shape)
    



    INIT_LR = 1e-3
    epochs = 10
    batch_size = 64
    

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, kernel_size=(3, 3),activation='relu',padding='same',input_shape=(100,100,3)),
        tf.keras.layers.LeakyReLU(alpha=0.1),
        tf.keras.layers.MaxPooling2D((2, 2),padding='same'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2,activation = 'softmax'),
        

        
        
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),loss='sparse_categorical_crossentropy',metrics=['accuracy'])

    history= model.fit(imagenes,labels,epochs=40,verbose=True)
    model.save('modelKeras/entrenado.h5')
    test_eval = model.evaluate(imagenes, labels, verbose=1)
    
    
    print('Test loss:', test_eval[0])
    print('Test accuracy:', test_eval[1])

    img = Image.open(rutaPrueba).resize((100,100))
    
    img = np.asarray(img)
    img = np.array([img])
    predict = model.predict(img)
    return categorias[np.argmax(predict[0])]
 
 
def convolucionarGuardado(rutaPrueba:str):
    
    categorias = []
    labels = [];
    imagenes = [];

    categorias = os.listdir("objetos/");

    x= 0
    for directorio in categorias:
        for imagen in os.listdir("objetos/"+directorio):
            img = Image.open("objetos/"+directorio+"/"+imagen).resize((100,100))
            img = np.asarray(img)
            imagenes.append(img)
            labels.append(x)
        x+=1
    imagenes = np.array(imagenes,dtype=np.uint8);

    labels = np.asarray(labels)
    

    model = keras.models.load_model('modelKeras/entrenado.h5')
    test_eval = model.evaluate(imagenes, labels, verbose=1)
    
    
    print('Test loss:', test_eval[0])
    print('Test accuracy:', test_eval[1])

    img = Image.open(rutaPrueba).resize((100,100))
    
    img = np.asarray(img)
    img = np.array([img])
    predict = model.predict(img)
    return categorias[np.argmax(predict[0])]

