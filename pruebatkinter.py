import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana en VS Code")
ventana.geometry("300x200")

# Agregar una etiqueta de texto
etiqueta = tk.Label(ventana, text="¡Tkinter funciona perfectamente!")
etiqueta.pack(pady=50)

# Iniciar el bucle de la aplicación
ventana.mainloop()
