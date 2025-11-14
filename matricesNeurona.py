import numpy as np

w = [[0.8, 0.4, 0.3, 0.2],
    [0.1, 0.7, 0.5, 0.3],
    [0.2, 0.8, 0.4, 0.9]]

x = [0.4, 0.8, 0.9, 0.7]

w = np.transpose(w)

multiplicacion = np.matmul(x,w)
print("Multiplicacion: ", multiplicacion)