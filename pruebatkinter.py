import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk() #crea una instancia de la clase Tk que representa la ventana principal de la aplicación
ventana.title("Mi primera ventana en VS Code") #titulo de la ventana 
ventana.geometry("300x200") #tamaño de la ventana en píxeles (ancho x alto) 

# Agregar una etiqueta de texto
etiqueta = tk.Label(ventana, text="¡Tkinter funciona perfectamente!") #lo que se mostrará en la ventana
etiqueta.pack(pady=50) #padding vertical de 50 píxeles etiqueta.pack es para empaquetar la etiqueta en la ventana 

# Iniciar el bucle de la aplicación
ventana.mainloop() #iniciar el bucle de la aplicación para que la ventana se mantenga abierta y responda a eventos
