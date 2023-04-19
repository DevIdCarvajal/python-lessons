# Soluciones rápidas

1

    class Coche:
      def __init__(self, marca, modelo, matricula):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
    
    miCoche = Coche("Tesla", "Model XD", "C3PO-R2D2")

2

    class Casa:
      def __init__(self, codPostal, calle, portal, piso):
        self.codPostal = codPostal
        self.calle = calle
        self.portal = portal
        self.piso = piso
    
    miCasa = Casa("28001", "Falsa", 1, 2)

3

    class PythonDeveloper:
      def __init__(self, listaProyectos):
        self.listaProyectos = listaProyectos
    
    yo = PythonDeveloper(["Python Básico", "Python Avanzado"])

4

    import random
    
    class Perro:
      def __init__(self, nombre, raza, color, edad):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad
      
      def ladrar(self):
        print("Woff, woff!")
      
      def hacerPopo(self):
        print(random.randrange(0, 3))
    
    miPerro = Perro("De San Roque", "Bodeguero", "Blanco", 2)

5

    class Noticia:
      def __init__(self, titular, cuerpo):
        self.titular = titular
        self.cuerpo = cuerpo
    
    miPerro = Noticia("No somos nadie", "Y nunca lo seremos")

6

    class Persona:
      def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    miColega = Persona("Bender", "Bending Rodríguez", 3)

7

    class Avion:
      def __init__(self, numPasajeros):
        self.numPasajeros = numPasajeros
      
      def volar(self):
        print("Llegando al destino")
      
      def aterrizar(self):
        print("Aterrizando")
    
    miAvion = Avion(200)

8

    class Paquete:
      def __init__(self, objetos):
        self.objetos = objetos
    
    miPaquete = Paquete(["cosa", 5, True])

9

    class Pais:
      def __init__(self, numHabitantes, continente, gentilicio):
        self.numHabitantes = numHabitantes
        self.continente = continente
        self.gentilicio = gentilicio
    
    miPais = Pais(47615034, "Europa", "Español"])

10

    marcaPortatil = Portatil.marca

11

    grupos = Concierto.listaGrupos

12

    tuplaRGB = (Led.rojo, Led.verde, Led.azul)

13

    codError = OhNoError.codigo

14

    integrantes = Grupo.listaIntegrantes

15

    nivelesTinta = Impresora.tinta

16

    pixeles = Ventana.dimensiones

17

    Portatil.modelo = "P345"

18

    Concierto.cartelera = "Guns N' Roses"

19

    from datetime import date
    
    Concierto.fecha = date.today()

20

    Impresora.imprimiendo = { "nombreArchivo": "dummy.txt", "copias": 5, "numPaginas": 10 }

21

    Grupo.numIntegrantes = 5

22

    Ventana.dimensiones = ((640, 480), (120, 80))

23

    Led.encendido = not Led.encendido

24

    Movil.temperatura = "20º"