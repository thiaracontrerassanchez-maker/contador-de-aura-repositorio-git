# 
from src.video_source import abrir_camara, mostrar_camara 
def main(): 
    camara = abrir_camara() 
    mostrar_camara(camara) 

if __name__ == "__main__":
    main() 