#interfaz grafica con tkinter 
import tkinter as tk

import tkinter.font as tkFont

window = tk.Tk() 
window.title("CONTADOR DE AURA")
window.geometry("1920x1080")
tkFont.nametofont("tkDefaultFont").configure(size=20)

etiqueta = tk.Label(window, text="Bienvenido al contador de aura")
etiqueta.pack(pady=50)


window.mainloop() 