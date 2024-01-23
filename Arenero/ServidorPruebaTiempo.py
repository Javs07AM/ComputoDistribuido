#!/usr/bin/env python

import socket
import threading
import time

def handle_client(cli, addr):
    print("Conexión establecida con la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

    while True:
        # Recibimos el mensaje
        recibido = cli.recv(1024)

        if not recibido:
            break

        # Imprimimos la IP y el mensaje recibido
        print("Recibido de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]) + ": " + recibido.decode())

        # Devolvemos el mensaje al cliente
        cli.send("Mensaje recibido".encode())

    # Cerramos la conexión con el cliente
    print("Conexión cerrada con la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
    cli.close()

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(('0.0.0.0', 443))
ser.listen(7)

print("Servidor esperando conexiones...")

while True:
    # Medimos el tiempo de conexión
    connection_start_time = time.time()

    # Aceptamos conexiones entrantes
    cli, addr = ser.accept()

    connection_end_time = time.time()

    print("Conexión aceptada desde la IP:", addr[0], "Puerto:", addr[1])
    print("Tiempo de conexión:", connection_end_time - connection_start_time, "segundos")

    # Creamos un hilo para manejar el cliente
    client_handler = threading.Thread(target=handle_client, args=(cli, addr))
    client_handler.start()