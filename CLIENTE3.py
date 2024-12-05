import socket

#ruta del archivo que tiene los mensajes codificados
RUTA_ARCHIVO = "mensaje.txt"
#el diccionario que ocupara para decodificar
diccionario = {
    'sigma': 'A', 'skibidi': 'B', 'gigachad': 'C', 'mewing': 'D', 'rizz': 'E',
    'gyatt': 'F', 'elfa': 'G', 'pomni': 'H', 'potaxie': 'I', 'gogogo': 'J',
    'momazo': 'K', 'simp': 'L', 'cringe': 'M', 'aimep3': 'N', 'lol': 'Ñ',
    'basado': 'O', 'papu': 'P', 'ternure68': 'Q', 'xiaohongshuuuu': 'R',
    'chiwis': 'S', 'speakerman': 'T', 'toilet': 'U', 'doomentio': 'V',
    'sdlg': 'W', 'unsaludoalagrasaaaaa': 'X', 'etesech': 'Y', 'xokas': 'Z',
    'chamba': '0', 'polancoas': '1', 'renegul': '2', 'fornite': '3',
    'skibiditoilet': '4', 'tilin': '5', 'cavifax': '6', 'noaptoparasensibles': '7',
    'wholesome': '8', 'puchaina': '9', 'void': ' ',
    '23casi24años': 'Á', 'holayosoymateo': 'É', 'aiaiaiaiai': 'Í',
    ':v': 'Ó', 'xdxdxddddd': 'Ú', 'digitalcircus': '.', 'ohio': ',',
    'ohmygodfloo': '!', 'rubentuesta': '¡', 'hastaluegopadres': '?',
    'losamopadres': '¿', 'desmotivaciones': ':', 'añañin': ';',
    'elpantera': '-', 'sigmalleros': '_', 'chaqueta': '(', 'insana': ')',
    'tiktok': '"'
}

#funcion para decodificar el mensaje codificado
def decodificar_texto(mensaje_codificado):
    palabras = mensaje_codificado.strip().split()  #divide el contenido del archivo en palabras
    mensaje_decodificado = ''.join(diccionario.get(palabra, palabra) for palabra in palabras)
    return mensaje_decodificado


with open(RUTA_ARCHIVO, 'r') as archivo:
     mensaje_codificado = archivo.read().strip() #lee el mensaje codificado en el archivo
    
print("se creo la conexion\n")
print(f"el mensaje codificado es {mensaje_codificado}")
    
mensaje_decodificado = decodificar_texto(mensaje_codificado) #decodifica el mensaje
print(f"el mensaje decodificado es {mensaje_decodificado}")

