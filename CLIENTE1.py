import socket

HOST = '127.0.0.1'  #se define la direccion y puerto del servidor
PORT = 8080         

#se crea el socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    #se conecta con el servidor
    cliente.connect((HOST, PORT))
    print("conexion creada")

    #se identifica
    cliente.sendall("CLIENTE_1".encode('utf-8'))  

    #pide mensaje
    mensaje = input("escribe el mensaje ")

    #se envia el mensaje al servidor
    cliente.sendall(mensaje.encode('utf-8'))
    print("se envio el mensaje al servidor")
