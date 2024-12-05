import socket
import threading

RUTA_ARCHIVO = "mensaje.txt"

#se hace mutex para sincronizar el acceso al archivo
lock = threading.Lock()

def manejar_cliente(conexion, direccion):
    print(f"el cliente se ha conectado en {direccion}") #se conecta al cliente

    tipo_cliente = conexion.recv(1024).decode('utf-8') #se identifica al cliente
    print(f"el cliente es {tipo_cliente}")

    if tipo_cliente == "CLIENTE_1":   #se verifica que cliente es, y dependiendo del que sea, se hace una operacion diferente
        manejar_escritura(conexion)
    elif tipo_cliente == "CLIENTE_2":
        manejar_lectura(conexion)

    conexion.close()
    print(f"conexion con {direccion} cerrada") #se anuncia el cierre de la conexion con un cliente

def manejar_escritura(conexion): #recibe un mensaje del cliente 1 y lo guarda en el archivo
    mensaje = conexion.recv(1024).decode('utf-8')
    print(f"el mensaje recibido de cliente 1 es {mensaje}")
    with lock:
        with open(RUTA_ARCHIVO, 'w') as archivo:
            archivo.write(mensaje)
    print(f"el mensaje se ha guardado en {RUTA_ARCHIVO}")

def manejar_lectura(conexion): #envia el contenido del archivo al cliente 2
    with lock: #manejo de excepciones
        try:
            with open(RUTA_ARCHIVO, 'r') as archivo:
                contenido = archivo.read().strip()
        except FileNotFoundError:
            contenido = ""  #en caso de que ei archivo no exista se envia un mensaje vacío
    print(f"se le envia al cliente 2 el contenido {contenido}")
    conexion.sendall(contenido.encode('utf-8'))

HOST = '127.0.0.1' #se definen la ip y puerto del servidor
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: #se crea el socket
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"el servidor anda a la escucha en {HOST}:{PORT}")  #se pone en modo de escucha

    while True:  #para que nunca termine
        conexion, direccion = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion)) #se hace un hilo por cada cliente y se comienza
        hilo.start()
