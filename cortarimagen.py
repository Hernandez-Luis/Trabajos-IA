import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imagen = cv.imread("amlo.jpg")



imgcpy = imagen.copy()
pmax = np.max(imagen)
pmin = np.min(imagen)

m = 255 / (pmax - pmin)
b = -m * pmin

#Esto es con numpy, pero no funciona
# imgcpy = np.add(np.multiply(m,imagen),b) 

#Esto es de una manera tradicional pero es mas tardado
w,h,_ = np.shape(imagen)

for i in range(w):
    for j in range(h):
        x = imagen [i][j]
        y = m*x + b
        imgcpy[i][j] = y

cv.imshow("Recortada", imgcpy); cv.waitKey(0); cv.destroyAllWindows()