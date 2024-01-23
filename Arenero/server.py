#!/usr/bin/env python
 
import socket
 
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("paso 1")

ser.bind(('0.0.0.0', 443))
 
print("paso 2")
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)
 
#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()

print("paso 3")
while True:

    #Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
    recibido = cli.recv(1024)

    print("paso 4")
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

    print("paso 5")
    #Devolvemos el mensaje al cliente
    cli.send("mensaje recibido")

#Cerramos la instancia del socket cliente y servidor
cli.close()
ser.close()

print("Conexiones cerradas")