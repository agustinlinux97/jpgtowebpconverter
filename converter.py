import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para seleccionar archivos
def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(
        title="Seleccionar imágenes JPEG",
        filetypes=[("Archivos JPEG", "*.jpeg *.jpg *.JPG *.JPEG")]
    )
    if archivos:
        convertir_imagenes(archivos)

# Función para convertir imágenes
def convertir_imagenes(archivos):
    for ruta_jpeg in archivos:
        try:
            # Abre la imagen JPEG
            with Image.open(ruta_jpeg) as imagen:
                # Cambia la extensión del archivo de .jpeg a .webp
                nombre_archivo_sin_extension = os.path.splitext(ruta_jpeg)[0]
                ruta_webp = nombre_archivo_sin_extension + ".webp"

                # Guarda la imagen en formato WebP
                imagen.save(ruta_webp, "webp")

                # Imprimir la ruta de guardado
                print(f"Convertido: {os.path.basename(ruta_jpeg)} a WebP en {ruta_webp}")

                # Verificar si el archivo fue guardado correctamente
                if os.path.exists(ruta_webp):
                    print(f"El archivo se guardó correctamente en {ruta_webp}")
                else:
                    print(f"Error al guardar el archivo {ruta_webp}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir {os.path.basename(ruta_jpeg)}: {str(e)}")
    
    # Mostrar mensaje de éxito
    messagebox.showinfo("Conversión completa", "Las imágenes han sido convertidas a WebP.")

# Configuración de la interfaz gráfica
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Convertidor de Imágenes a WebP")

    label = tk.Label(ventana, text="Seleccione las imágenes JPEG para convertir")
    label.pack(pady=10)

    boton_seleccionar = tk.Button(ventana, text="Seleccionar imágenes", command=seleccionar_archivos)
    boton_seleccionar.pack(pady=10)

    ventana.geometry("400x200")
    ventana.mainloop()

# Ejecutar la interfaz gráfica
crear_interfaz()
