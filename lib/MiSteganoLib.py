"""
 by Edward Lopez
"""
from cryptosteganography import CryptoSteganography
import random
import string
import filetype

# Clase de Esteganografía con el objetivo de hacer múltiples pruebas


class MiSteganoLib:

    # Variables privadas
    key: str
    imageContainerPath: str
    steganoImagePath: str

    # Inicialización de la clase, se le indica la clave y se puede o no enviar una imagen contenedora.
    def __init__(self, key: str, imageContainerPath: str = None):
        self.key = key

        # Imagen de un retablo ayacuchano, se usará por defecto en caso no se mandé imagenes al clase
        # Mi bisabuelo creó en el año 1945 el retablo Ayacuchano, quería aprovechar el ejercicio
        # para compartir un poco de su arte y aprovechar una imagen pesada que tomé de uno de sus
        # trabajos.

        self.imageContainerPath = "./container/ayacucho_starter_pack.png" if(
            imageContainerPath == None) else imageContainerPath

    # Método para esconder una archivo cualquiera o mensaje, se debe indicar si es archivo y pasar
    # la ruta del archivo o el mensaje a esconder en una cadena.
    def hideFileorMessage(self, isFile: bool, messageOrFilePath: str):

        randomNameFile = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=10))

        self.steganoImagePath = "./out/{0}.png".format(randomNameFile)

        mySecretMessage = messageOrFilePath

        if isFile:
            with open(messageOrFilePath, "rb") as f:
                mySecretMessage = f.read()

        crypto_steganography = CryptoSteganography(self.key)
        crypto_steganography.hide(
            self.imageContainerPath, self.steganoImagePath, mySecretMessage)

        print("Se generó la imagen con la técnica de esteganografía en la siguiente ruta: {0}".format(
            self.steganoImagePath))

    # Método permite obtener el mensaje o archivo escondido en la imagen contenedora
    def getFileorMessageFormImageContainer(self, imageContainer: str):
        crypto_steganography = CryptoSteganography(self.key)
        print("Procesando el resultado....")
        secretInBytes = crypto_steganography.retrieve(imageContainer)

        print("La imagen contenedora tenía un mensaje....")

        try:
            extension = filetype.guess_extension(secretInBytes)

            if(extension == None):
                print("El mensaje es: '{0}'".format(secretInBytes))
                return
        except:
            print("El mensaje es: '{0}'".format(secretInBytes))
            return

        randomNameFile = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=10))

        savePath = "./decrypted_files/"

        with open('{0}{1}.{2}'.format(savePath, randomNameFile, extension), 'wb') as f:
            f.write(secretInBytes)

        print("El archivo se guardó en la ruta {0}{1}.{2}".format(
            savePath, randomNameFile, extension))

        # print("El mensaje es el siguiente: {0}".format(secretInBytes))
