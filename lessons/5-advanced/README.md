# 5. Técnicas avanzadas:

## Índice

[1. Manejo de excepciones](#1-manejo-de-excepciones)  
[2. Gestión de paquetes](#2-gestion-de-paquetes)  
[3. Entrada/salida de datos](#3-entrada-salida-de-datos)  
[4. Expresiones regulares](#4-expresiones-regulares)  
[5. Serialización de objetos](#5-serializacion-de-objetos)

## 1. Manejo de excepciones

[Coming soon]

## 2. Gestión de paquetes

[Coming soon]

## 3. Entrada/salida de datos

[Coming soon]

## 4. Expresiones regulares

[Coming soon]

## 5. Serialización de objetos

Serializar una lista en un fichero:

```
import pickle

myFile = open("animalsFile.dat", "wb")

animals = ["python", "monkey", "camel"]

pickle.dump(animals, myFile)  

myFile.close()
```

Deserializar una lista de un fichero:

```
import pickle

myFile = open("animalsFile.dat", "rb")

animals = pickle.load(myFile)

print(animals)

myFile.close()
```

Y para poder guardar datos de indexación como un objeto clave-valor:

```
import shelve

myGodShelf = shelve.open("god.dat")

myGodShelf['name'] = "Azatoth"
myGodShelf['age'] = 13787
myGodShelf['immortal'] = True

myGodShelf.close()
```

Y leerlos de nuevo:

```
import shelve

myGodShelf = shelve.open("god.dat")

print(myGodShelf['name'])
print(myGodShelf['age'])
print(myGodShelf['immortal'])

myGodShelf.close()
```

## Referencias

[Manejo de excepciones](https://www.w3schools.com/python/python_try_except.asp)  
[Gestor de paquetes](https://www.w3schools.com/python/python_pip.asp)  
[Módulos](https://www.w3schools.com/python/python_modules.asp)  
[Manejo de ficheros](https://www.w3schools.com/python/python_file_handling.asp)  
[Argumentos por línea de comandos](https://www.pythonforbeginners.com/system/python-sys-argv)  
[Referencia regex](https://regexr.com/)  
[El módulo re](https://www.w3schools.com/python/python_regex.asp)  
OBSOLETO: [Serialización de objetos](http://mundogeek.net/archivos/2008/05/20/python-serializacion-de-objetos/)
