import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imagen = cv.imread("amlo.jpg")
imagengris = cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
# cv.imshow("Monocromatica", imagengris); cv.waitKey(0); cv.destroyAllWindows()

imgsize = cv.resize(imagengris, (200,200)) 
np.max(imgsize)
np.min(imgsize) 

hist = cv.calcHist([imagen],[0], None, [256], [0,256])

plt.figure(figsize=(8,4))
plt.title("Histograma en Escala de Grises")
plt.xlabel("Nivel de intensidad (0-255)")
plt.ylabel("Cantidad de píxeles")
plt.plot(hist)
plt.xlim([0,256])
plt.show()