import socket

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

RUTA_ARCHIVO = "mensaje.txt"

def codificar_mensaje(mensaje):
    """Codifica un mensaje usando el diccionario."""
    return ' '.join(diccionario.get(caracter.upper(), caracter) for caracter in mensaje)

def guardar_en_archivo(mensaje_codificado):
    """Guarda el mensaje codificado en el archivo."""
    with open(RUTA_ARCHIVO, 'w') as archivo:
        archivo.write(mensaje_codificado)
    print(f"Se guardó en {RUTA_ARCHIVO}: {mensaje_codificado}")

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    print("Conexión creada")
    cliente.sendall("CLIENTE_2".encode('utf-8'))  

    mensaje = cliente.recv(1024).decode('utf-8').strip()
    if not mensaje:
        print("Error: No se recibió mensaje del servidor.")
    else:
        print(f"Mensaje recibido del servidor: {mensaje}")


        mensaje_codificado = codificar_mensaje(mensaje)
        print(f"Mensaje codificado: {mensaje_codificado}")

        guardar_en_archivo(mensaje_codificado)

        cliente.sendall(mensaje_codificado.encode('utf-8'))
        print("Mensaje codificado enviado al servidor")
