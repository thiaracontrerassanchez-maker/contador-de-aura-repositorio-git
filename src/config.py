#configuracion del programa, como calibracion de la camara, etc.

import cv2 as cv
import numpy as np 
import glob 


COLUMNAS_INTERNAS = 7
FILAS_INTERNAS = 5
LADO_CUADRADO_MM = 25.0  # ajustá al tamaño real impreso

criterios = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

puntos_objeto_3d = np.zeros((COLUMNAS_INTERNAS * FILAS_INTERNAS, 3), np.float32)
puntos_objeto_3d[:, :2] = np.mgrid[0:COLUMNAS_INTERNAS, 0:FILAS_INTERNAS].T.reshape(-1, 2)
puntos_objeto_3d *= LADO_CUADRADO_MM

object_points, image_points = [], []
imagenes = glob.glob('calibracion/*.jpg')
if not imagenes:
    raise SystemExit("No se encontraron imágenes en calibracion/*.jpg")

tam_imagen = None
flags = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE

for ruta in imagenes:
    img = cv.imread(ruta)
    if img is None:
        print(f"No se pudo leer {ruta}")
        continue
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    tam_imagen = gray.shape[::-1]

    ok, esquinas = cv.findChessboardCorners(gray, (COLUMNAS_INTERNAS, FILAS_INTERNAS), flags)
    if not ok:
        print(f"Sin tablero detectado: {ruta}")
        continue

    esquinas = cv.cornerSubPix(gray, esquinas, (11, 11), (-1, -1), criterios)
    object_points.append(puntos_objeto_3d)
    image_points.append(esquinas)

    cv.drawChessboardCorners(img, (COLUMNAS_INTERNAS, FILAS_INTERNAS), esquinas, ok)
    cv.imshow('Esquinas Detectadas', img)
    cv.waitKey(300)

cv.destroyAllWindows()

if len(object_points) < 10:
    print(f"Advertencia: solo {len(object_points)} imágenes válidas (se recomiendan 10-20+)")
if not object_points:
    raise SystemExit("No se detectó el tablero en ninguna imagen")

rms, mtx, dist, rvecs, tvecs = cv.calibrateCamera(object_points, image_points, tam_imagen, None, None)

# Error de reproyección por imagen
for i in range(len(object_points)):
    proy, _ = cv.projectPoints(object_points[i], rvecs[i], tvecs[i], mtx, dist)
    err = cv.norm(image_points[i], proy, cv.NORM_L2) / len(proy)
    print(f"Imagen {i}: error {err:.4f} px")

print("RMS global:", rms)
print("Matriz de la cámara:\n", mtx)
print("Distorsión:\n", dist)

np.savez('calibracion.npz', mtx=mtx, dist=dist)


