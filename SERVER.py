import socket
import threading

# Ruta del archivo compartido
RUTA_ARCHIVO = "mensaje.txt"

# Lock para sincronizar el acceso al archivo
lock = threading.Lock()

def manejar_cliente(conexion, direccion):
    print(f"Cliente conectado desde {direccion}")

    # Recibir identificación del cliente
    tipo_cliente = conexion.recv(1024).decode('utf-8')
    print(f"Cliente identificado como: {tipo_cliente}")

    if tipo_cliente == "CLIENTE_1":
        manejar_escritura(conexion)

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
