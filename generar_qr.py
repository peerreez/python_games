import tkinter as tk
import qrcode
from PIL import ImageTk, Image

def generar_codigo_qr():
    texto = entrada_texto.get()
    
    # Crear un objeto QRCode
    codigo_qr = qrcode.QRCode(
        version=1,  # Tamaño del código QR (1 a 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Tamaño de cada "box" en el código QR
        border=4,  # Ancho del borde del código QR
    )

    # Agregar el texto al código QR
    codigo_qr.add_data(texto)
    codigo_qr.make(fit=True)

    # Crear una imagen PIL (Python Imaging Library) del código QR
    imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

    # Convertir la imagen PIL a formato compatible con Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_qr)

    # Actualizar la etiqueta con la nueva imagen
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Códigos QR")

# Crear un widget de entrada de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=10)

# Crear un botón para generar el código QR
boton_generar = tk.Button(ventana, text="Generar Código QR", command=generar_codigo_qr)
boton_generar.pack(pady=10)

# Crear una etiqueta para mostrar la imagen del código QR
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
