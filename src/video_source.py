import cv2
from src.config import CAMARA_ID, ANCHO_CAMARA, ALTO_CAMARA 

def abrir_camara():
    cap = cv2.VideoCapture(CAMARA_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ANCHO_CAMARA)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ALTO_CAMARA)
    if not cap.isOpened():
        raise SystemExit("No se pudo abrir la cámara")
    return cap  

def mostrar_camara(cap): 
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame de la cámara")
            break
        frame = cv2.flip(frame, 1)  # Voltear horizontalmente 
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        cv2.imshow("Cámara", gris)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

    cap.release()  
    cv2.destroyAllWindows() 