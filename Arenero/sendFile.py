import socket
import time

def enviar_archivo(sock, nombre_archivo):
    # Enviamos el comando al servidor
    sock.send('enviar'.encode())
    time.sleep(0.1)

    # Enviamos el nombre del archivo al servidor
    sock.send(nombre_archivo.encode())
    time.sleep(0.1)

    # Abrimos el archivo y enviamos su contenido al servidor
    with open(nombre_archivo, 'rb') as file:
        for data in iter(lambda: file.read(1024), b''):
            sock.sendall(data)
            time.sleep(0.1)

def recibir_archivo(sock, nombre_archivo):
    # Enviamos el comando al servidor
    sock.send('recibir'.encode())
    time.sleep(0.1)

    # Enviamos el nombre del archivo al servidor
    sock.send(nombre_archivo.encode())
    time.sleep(0.1)

    # Creamos el archivo y recibimos el contenido del servidor
    with open(nombre_archivo, 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)
            time.sleep(0.1)

# Conéctate al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.40.1', 443))

# Prueba de envío de archivo
enviar_archivo(cliente, 'texto.txt')

# Prueba de recepción de archivo
recibir_archivo(cliente, 'p.txt')
# Cierra la conexión
cliente.close()