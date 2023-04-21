# 6. Programación paralela

## Índice

[1. Sockets](#1-sockets)  
[2. Threads](#2-threads)

## 1. Sockets

Cuando dos aplicaciones o procesos interactúan, utilizan un canal de comunicación específico. Los sockets son los puntos finales o puntos de entrada de dichos canales de comunicación.

Podemos usar sockets para establecer un canal de comunicación entre dos procesos, dentro de un proceso o entre procesos en diferentes máquinas.

Python nos proporciona el módulo `socket` para implementar la programación de sockets. El módulo socket es parte de la biblioteca estándar de Python y proporciona todas las funciones y métodos con la ayuda de los cuales puede crear sockets en Python.

Ejemplo de cliente:

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

Ejemplo de servidor:

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

## 2. Threads

En el ámbito de la programación concurrente, también llamada paralela, se manejan los conceptos de multiprocesamiento y multihilo (multithreading) para realizar varias tareas "al mismo tiempo" o, mejor dicho, concurrentemente.

Esto significa que en el primer caso las tareas sí se ejecutan al mismo tiempo (como procesos), ya que hay varios procesadores (núcleos) para realizarlas, mientras que en el segundo se trata de una sensación más o menos percibida a partir del reparto continuo del procesador entre los distintos hilos de ejecución.

Si un proceso es un programa en ejecución, los hilos son subprocesos creados por un proceso superior, con los que comparte un supercontexto global y a los que otorga a cada uno su propio contexto (variables, etc.), de manera que además se puedan comunicar entre sí.

En Python se pueden generar y ejecutar procesos fácilmente a partir de funciones:

    import threading

    def print_cube(num):
      print(f"Cubo: {num * num * num}")

    def print_square(num):
      print(f"Cuadrado: {num * num}")

    # Ejecutado solo en el programa principal
    if __name__ =="__main__":
      
      # Crear threads
      t1 = threading.Thread(target=print_square, args=(10,))
      t2 = threading.Thread(target=print_cube, args=(10,))

      # Ejecutar threads
      t1.start()
      t2.start()

      # Esperar a la finalización de los threads
      t1.join()
      t2.join()

      print("Fin del programa")

Tanto los procesos (incluyendo el del programa principal) como los threads tienen un nombre así como un identificador (pid), que es posible conocer:

    import threading
    import os

    def task1():
      print(f"Tarea 1 - Thread {threading.current_thread().name}")
      print(f"pid del proceso de la tarea 1: {os.getpid()}")

    def task2():
      print(f"Tarea 2 - Thread {threading.current_thread().name}")
      print(f"pid del proceso de la tarea 2: {os.getpid()}")

    if __name__ == "__main__":

      print(f"Programa principal - Thread {threading.current_thread().name}")
      print(f"pid del proceso del programa principal: {os.getpid()}")

      t1 = threading.Thread(target=task1, name='tarea1')
      t2 = threading.Thread(target=task2, name='tarea2')

      t1.start()
      t2.start()

      t1.join()
      t2.join()

En ocasiones dos o más hilos acceden a los mismos recursos compartidos (también llamados secciones críticas), lo que puede originar condiciones de carrera, que implican resultados distintos dependiendo de qué hilo accedió primero:

    import threading

    def task1():
      for i in range(5):
        print('Tarea 1')
    
    def task2():
      for i in range(5):
        print('Tarea 2')

    if __name__=="__main__":
      t1 = threading.Thread(target=task1)
      t2 = threading.Thread(target=task2)

      t1.start()
      t2.start()

      t1.join()
      t2.join()

Para evitar esto, existen diversos mecanismos como los semáforos o el del siguiente ejemplo, conocido como bloqueo (`Lock`), cerrojo o exclusión mutua:

    import threading
    lock = threading.Lock()

    def task1():
      lock.acquire()

      for i in range(5):
        print('Tarea 1')
      
      lock.release()
    
    def task2():
      lock.acquire()

      for i in range(5):
        print('Tarea 2')
      
      lock.release()

    if __name__=="__main__":
      t1 = threading.Thread(target=task1)
      t2 = threading.Thread(target=task2)

      t1.start()
      t2.start()

      t1.join()
      t2.join()

## Referencias

[Programación de sockets en Python](https://www.delftstack.com/es/howto/python/socket-programming-in-python-a-beginners-guide/)  
[tutorialspoint: Sockets](https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm)  
[Multithreading in Python Example I](https://www.geeksforgeeks.org/multithreading-python-set-1/)  
[Multithreading in Python Example II](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)