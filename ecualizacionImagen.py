import cv2
import numpy as np

imagen = cv2.imread("imgPython.png", cv2.IMREAD_GRAYSCALE)
alto, ancho = imagen.shape

ecualizada = np.zeros_like(imagen, dtype=np.uint8)

hist = np.zeros(256, dtype=np.int32)
for fila in range(alto):
    for col in range(ancho):
        hist[imagen[fila, col]] += 1

cdf = np.cumsum(hist)

cdf_normalizada = ((cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())).astype(np.uint8)

for fila in range(alto):
    for col in range(ancho):
        ecualizada[fila, col] = cdf_normalizada[imagen[fila, col]]

cv2.imshow("Original vs Ecualizada", cv2.hconcat([imagen, ecualizada]))
cv2.waitKey(0)
cv2.destroyAllWindows()