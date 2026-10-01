#configuracion del programa, como calibracion de la camara, etc.

import cv2 as cv
import numpy as np 

COLUMNAS_INTERNAS = 7
FILAS_INTERNAS = 5
LADO_CUADRADO_MM = 25.0  # ajustá al tamaño real impreso

criterios = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)