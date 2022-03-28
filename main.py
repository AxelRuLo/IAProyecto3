import os
from skimage.transform import resize
import numpy as np
import re
import matplotlib.pyplot as plt
# import convolucional


dirname = os.path.join(os.getcwd(), "objetos")
imgpath = dirname + os.sep

images = []
imagesR = []
directories = []
dircount = []
prevRoot = ""
cant = 0


print("leyendo imagenes de ", imgpath)

for root, dirnames, filenames in os.walk(imgpath):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            cant = cant + 1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            b = "Leyendo..." + str(cant)
            print(b, end="\r")
            if prevRoot != root:
                print(root, cant)
                prevRoot = root
                directories.append(root)
                dircount.append(cant)
                cant = 0
dircount.append(cant)

for i in range(len(images)):
    res = resize(images[i], (1000, 800))
    imagesR.append(res)


print("shape")
for i in range(len(imagesR)):
    print(imagesR[i].shape)


dircount = dircount[1:]
dircount[0] = dircount[0] + 1


# historialConvolucional = convolucional.convolucionar(images,directories,dircount,prevRoot,cant)
