#ejercicio 17 sem_03 - 04

import numpy as np

def matriz_covarianza(X, Y):
    media_X = np.mean(X, axis=0)
    media_Y = np.mean(Y, axis=0)
    
    desviacion_X = X - media_X
    desviacion_Y = Y - media_Y
    
    covarianza = np.dot(desviacion_X.T, desviacion_Y) / X.shape[0]
    
    return covarianza

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

covarianza = matriz_covarianza(X, Y)
print(covarianza)