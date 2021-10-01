# 6. Programación paralela:

## Índice

[1. Sockets](#1-sockets)  
[2. Threads](#2-threads)

## 1. Sockets

Ejemplo de cliente:

```
import socket

s = socket.socket()

s.connect(("localhost", 9999))

while True:
    
    mensaje = input("Mensaje a enviar: ")

    s.send(mensaje.encode())

    if mensaje == "close":
        break

print("Taluego, servidor!")

s.close()
```

Ejemplo de servidor:

```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 9999))

s.listen(1)

sc, addr = s.accept()

while True:

    recibidoBytes = sc.recv(1024)
    recibido = recibidoBytes.decode()

    if recibido == "close":
        break

    print(str(addr[0]) + " dice: ", recibido)

    sc.send(recibidoBytes)

print("Taluego, cliente!")

sc.close()
s.close()
```

## 2. Threads

[Coming soon]

## Referencias

[Ejemplo de sockets](https://developeando.net/sockets-python/)  
[tutorialspoint: Sockets](https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm)  
[Multithreading in Python (with GIL)](https://www.guru99.com/python-multithreading-gil-example.html)  
[Multithreading in Python Example I](https://www.geeksforgeeks.org/multithreading-python-set-1/)  
[Multithreading in Python Example II](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)  
[tutorialspoint: Threads](https://www.tutorialspoint.com/python/python_multithreading.htm)
