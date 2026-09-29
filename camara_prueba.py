import cv2 #es para usar la camara (opencv)
camara = cv2.VideoCapture(0) #VideoCapture(0) abre la camara predeterminada del sistema (0 primera camara disponible), o sea que guarda en "camara" la primer camara de la computadora. Si que abrir otra camara, se pondria 1, 2, y asi, dependiendo de cuantas camaras tengamos
while True:#mientras sea verdadero 
    ret, frame = camara.read() #ret es para que nos diga si pudo obtener la imagen, frame es la imagen que se obtuvo de la camara
    if not ret:
        break #rompe el bucle obvio...
    cv2.imshow("Camara", frame) #imshow significa mostrar imagen, y camara es el nombre de la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'): #cv2.waitkey(1) espera 1 milisegundo para detectar una tecla, y si se presiona la tecla q (ord('q') se rompe el bucle con el break y cierra la ventana
        break
camara.release() #libera la camara
cv2.destroyAllWindows() #cierra todas las ventanas abiertas por opencv 
#& 0xFF es para que funcione en todas las versiones de python, ya que en algunas versiones de python, cv2.waitKey(1) devuelve un valor de 32 bits, y en otras devuelve un valor de 8 bits. Por eso se hace un AND con 0xFF para obtener solo los 8 bits menos significativos, que es lo que nos interesa.