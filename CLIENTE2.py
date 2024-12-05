import socket
#el diccionario que ocupara para codificar
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

RUTA_ARCHIVO = "mensaje.txt" #ruta del archivo a usar

def codificar_mensaje(mensaje): #codifica el mensaje usando el diccionario
    return ' '.join(diccionario.get(caracter.upper(), caracter) for caracter in mensaje)

def guardar_en_archivo(mensaje_codificado): #guarda el mensaje codificado en el archivo
    with open(RUTA_ARCHIVO, 'w') as archivo:
        archivo.write(mensaje_codificado)
    print(f"se ha guardado en {RUTA_ARCHIVO}: {mensaje_codificado}")

HOST = '127.0.0.1' #se define el host y el puerto
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #se crea el socket y se conecta
    cliente.connect((HOST, PORT))
    print("se ha conectado")
    cliente.sendall("CLIENTE_2".encode('utf-8'))   #se identifica a si mismo

    try: #manejo de excepciones
        with open(RUTA_ARCHIVO, 'r') as archivo:
            mensaje = archivo.read().strip()
            if not mensaje:
                print("el archivo esta vacio") #si no hay nada en el archivo dira que esta vacio
            else:
                print(f"el mensaje en el archivo es {mensaje}") #si si hay algo, lo leera

                mensaje_codificado = codificar_mensaje(mensaje)
                print(f"el mensaje codificado es {mensaje_codificado}") #y lo codificara

                guardar_en_archivo(mensaje_codificado) #y se  guarda en el archivo

                cliente.sendall(mensaje_codificado.encode('utf-8')) #se envia el mensaje codificado al servidor
                print("mensaje codificado enviado al servidor")
    except FileNotFoundError:
        print(f"el archivo {RUTA_ARCHIVO} no existe") #si el archivo no existe dara error
