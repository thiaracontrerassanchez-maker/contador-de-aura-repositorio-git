import cv2

# Muestra la versión instalada de OpenCV
print("Versión de OpenCV:", cv2.__version__)

# Crea una imagen negra de prueba (300x300 píxeles)
import numpy as np
imagen = np.zeros([300, 300, 3], dtype=np.uint8)

# Dibuja un texto en la imagen
cv2.putText(imagen, "OpenCV Funciona!", (20, 150), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Muestra la imagen en una ventana
cv2.imshow("Ventana de Prueba", imagen)

# Espera a que presiones una tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
