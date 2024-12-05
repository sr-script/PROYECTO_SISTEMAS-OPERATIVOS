import socket
import threading

RUTA_ARCHIVO = "mensaje.txt"

# Lock para sincronizar el acceso al archivo
lock = threading.Lock()

def manejar_cliente(conexion, direccion):
    print(f"Cliente conectado desde {direccion}")

    tipo_cliente = conexion.recv(1024).decode('utf-8')
    print(f"Cliente identificado como: {tipo_cliente}")

    if tipo_cliente == "CLIENTE_1":
        manejar_escritura(conexion)
    elif tipo_cliente == "CLIENTE_2":
        manejar_lectura(conexion)

    conexion.close()
    print(f"Conexión con {direccion} cerrada")

def manejar_escritura(conexion):
    """Recibe un mensaje de CLIENTE_1 y lo guarda en el archivo."""
    mensaje = conexion.recv(1024).decode('utf-8')
    print(f"Mensaje recibido de CLIENTE_1: {mensaje}")
    with lock:
        with open(RUTA_ARCHIVO, 'w') as archivo:
            archivo.write(mensaje)
    print(f"Mensaje guardado en {RUTA_ARCHIVO}")

def manejar_lectura(conexion):
    """Envía el contenido del archivo a CLIENTE_2."""
    with lock:
        try:
            with open(RUTA_ARCHIVO, 'r') as archivo:
                contenido = archivo.read().strip()
        except FileNotFoundError:
            contenido = ""  # Si el archivo no existe, enviar mensaje vacío
    print(f"Enviando contenido a CLIENTE_2: {contenido}")
    conexion.sendall(contenido.encode('utf-8'))

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conexion, direccion = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo.start()
