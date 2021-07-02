from lib.MiSteganoLib import MiSteganoLib

# DEMO - La Clase al ser inicializada, en caso no se le indique una ruta de imagen que será la contenedora,
# toma un archivo de 3.89MB, siempre el tamaño del criptograma generado del mensaje debe ser mejor al tamaño
# de la imagen.
#
# Esconde un audio
MiSteganoLib("Lo mejor de Ayacucho").hideFileorMessage(
    True, "./demo_files/mp3/ayac-musica-toril.mp3")

# Esconde un mensaje
MiSteganoLib("Lo mejor de Ayacucho",
             "./container/demo/pascua_2015.jpg").hideFileorMessage(False, "Bienvenido a Ayacucho")

# DEMO - Obtener mensajes o archivos ocultos de imágenes contenedoras
# Al finalizar la generación de una imagen contenedora, imprime el nombre
# de la nueva imagen generada en consola.
#
# MiSteganoLib("Lo mejor de Ayacucho").getFileorMessageFormImageContainer("./out/<indicarNombreAutogenerado>.png")


# Otras pruebas
# En caso se tenga una imagen contenedora y se quiere esconder cualquier tipo de archivo
# Siempre el tamaño de la imagen debe ser mayor al tamaño del criptograma del mensaje a ocultar
# MiSteganoLib("Lo mejor de Ayacucho","./<indicarRutaYNombreImagenContenedora>").hideFileorMessage(True, "./<indicarRutaYNombreArchivo>")
