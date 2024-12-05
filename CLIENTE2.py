import socket

#diccionario de codificacion
diccionario = {
    'A': 'sigma', 'B': 'skibidi', 'C': 'gigachad', 'D': 'mewing', 'E': 'rizz', 'F': 'gyatt',
    'G': 'elfa', 'H': 'pomni', 'I': 'potaxie', 'J': 'gogogo', 'K': 'momazo', 'L': 'simp',
    'M': 'cringe', 'N': 'aimep3', 'Ñ': 'lol', 'O': 'basado', 'P': 'papu', 'Q': 'ternure68',
    'R': 'xiaohongshuuuu', 'S': 'chiwis', 'T': 'speakerman', 'U': 'toilet', 'V': 'doomentio',
    'W': 'sdlg', 'X': 'unsaludoalagrasaaaaa', 'Y': 'etesech', 'Z': 'xokas',
    'Á': '23casi24años', 'É': 'holayosoymateo', 'Í': 'aiaiaiaiai', 'Ó': ':v', 'Ú': 'xdxdxddddd',
    '0': 'chamba', '1': 'polancoas', '2': 'renegul', '3': 'fornite', '4': 'skibiditoilet',
    '5': 'tilin', '6': 'cavifax', '7': 'noaptoparasensibles', '8': 'wholesome', '9': 'puchaina',
    ' ': 'void', '.': 'digitalcircus', ',': 'ohio', '!': 'ohmygodfloo', '¡': 'rubentuesta',
    '?': 'hastaluegopadres', '¿': 'losamopadres', ':': 'desmotivaciones', ';': 'añañin',
    '-': 'elpantera', '_': 'sigmalleros', '(': 'chaqueta', ')': 'insana', '"': 'tiktok'
}

#es en donde se guardara el mensaje codificado 
RUTA_ARCHIVO = "mensaje.txt"

def codificar_mensaje(mensaje): #codifica el mensaje
    return ' '.join(diccionario.get(caracter.upper(), caracter) for caracter in mensaje)


def guardar_en_archivo(mensaje_codificado): #se guarda el mensaje codificado en el archivo
    with open(RUTA_ARCHIVO, 'w') as archivo:
        archivo.write(mensaje_codificado)
    print(f"se guardo  en {RUTA_ARCHIVO}")

#se define la ip y puerto del servidor
HOST = '127.0.0.1' 
PORT = 8080        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #se crea el socket
    cliente.connect((HOST, PORT)) #se conecta el socket
    print("conexion creada")
    cliente.sendall("CLIENTE_2".encode('utf-8'))  #id del cliente


    mensaje = cliente.recv(1024).decode('utf-8')
    print(f"el mensaje recibido del servidor fue {mensaje}") #se obtiene el mensaje

    mensaje_codificado = codificar_mensaje(mensaje) #se codifica el mensaje
    print(f"el mensaje ha sido codificado a {mensaje_codificado}")

    guardar_en_archivo(mensaje_codificado) #se guarda el mensaje codificado
 
    cliente.sendall(mensaje_codificado.encode('utf-8')) #se envia el mensaje codificado al servidor
    print("mensaje enviado al servidor")
