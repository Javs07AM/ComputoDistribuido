from PIL import Image, ImageSequence

def desmontar_gif(ruta_gif, carpeta_destino):
    # Abre el archivo GIF
    gif = Image.open(ruta_gif)

    try:
        # Extrae todos los fotogramas del GIF
        fotogramas = [f.convert('RGBA') for f in ImageSequence.Iterator(gif)]

        # Guarda cada fotograma como una imagen separada
        for i, fotograma in enumerate(fotogramas):
            nombre_archivo = f"{carpeta_destino}/fotograma_{i}.png"
            fotograma.save(nombre_archivo, 'PNG')

        print(f"Se han desmontado {len(fotogramas)} fotogramas en la carpeta '{carpeta_destino}'.")
    except Exception as e:
        print(f"Error al desmontar el GIF: {e}")

# Ruta de tu archivo GIF
ruta_gif = 'C:\\xampp\\htdocs\\computoDistribuido\\ProyectoComputo\\marte.gif'

# Carpeta donde se guardarán los fotogramas
carpeta_destino = 'C:\\xampp\\htdocs\\computoDistribuido\\ProyectoComputo\\fotogramasMarte'


# Desmontar el GIF
desmontar_gif(ruta_gif, carpeta_destino)
