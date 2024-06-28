import tkinter as tk
from tkinter import scrolledtext  # Importar scrolledtext para usar un Text con barra de desplazamiento
import backend as bk

ventana = tk.Tk()

# Establecer las dimensiones de la ventana
ventana.geometry("1000x550")

# Establecer el color de fondo de la ventana
ventana.configure(bg="#E8DAEF")

# Título
h1 = tk.Label(ventana, text=bk.h1, bg="#E8DAEF", font=("Helvetica", 16))
h1.pack(padx=20, pady=10)

h2 = tk.Label(ventana, text=bk.h2, bg="#E8DAEF", font=("Helvetica", 14))
h2.pack(padx=20, pady=10)

h3 = tk.Label(ventana, text=bk.h3, bg="#E8DAEF", font=("Helvetica", 12))
h3.pack(padx=20, pady=10)

h4 = tk.Label(ventana, text=bk.h4, bg="#E8DAEF", font=("Helvetica", 12))
h4.pack(padx=20, pady=10)

h5 = tk.Label(ventana, text=bk.h5, bg="#E8DAEF", font=("Helvetica", 12))
h5.pack(padx=20, pady=10)

# Usuario ingrese datos
opcion_entry = tk.Entry(ventana, font=("Helvetica", 14))
opcion_entry.pack(padx=20, pady=10)

# Función
def submit():
    opcion_usuario = opcion_entry.get()
    print("Usuario ingresó:", opcion_usuario)
    mensaje = bk.procesar_opcion(opcion_usuario)  # Llamar a la función del backend
    mensaje_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
    mensaje_text.insert(tk.END, mensaje)  # Mostrar el mensaje en el widget Text

# Botón envío
submit_button = tk.Button(ventana, text="Enviar", command=submit, font=("Helvetica", 14))
submit_button.pack(padx=20, pady=10)

# Widget Text con barra de desplazamiento
mensaje_text = scrolledtext.ScrolledText(ventana, height=20, width=100, wrap=tk.WORD, font=("Helvetica", 12))
mensaje_text.pack(padx=20, pady=50)

# Etiqueta opcional para mostrar mensajes 
mensaje_label = tk.Label(ventana, text="", bg="#E8DAEF", font=("Helvetica", 10))
mensaje_label.pack(padx=20, pady=10)

ventana.mainloop()
