# Ejercicios rápidos

## Introducción

A continuación se ofrece una colección de ejercicios rápidos de programación para desarrollar en Python.

Aunque están planteados cubriendo un espectro de dificultad incremental, si te atascas mucho con uno pasa al siguiente y ya lo retomarás más adelante.

## Objetos

### Declaración

1. Crear una **clase** de nombre **Coche**  que tenga las propiedades **marca, modelo, matricula**, e instanciar un **objeto** de dicha clase
2. Crear una **clase** de nombre **Casa** que tenga las propiedades **codPostal, calle, portal, piso**, e instanciar un **objeto** de dicha clase
3. Crear una **clase** de nombre **PythonDeveloper** que tenga la propiedad **listaProyectos**, e instanciar un **objeto** de dicha clase
4. Crear una **clase** de nombre **Perro** que tenga las propiedades **nombre, raza, color, edad** y los métodos **ladrar (imprime por consola un ladrido) y hacerPopo (devuelve un valor aleatorio entre 0 y 2 incluidos)**, e instanciar un **objeto** de dicha clase
5. Crear una **clase** de nombre **Noticia** que tenga las propiedades **titular, cuerpo**, e instanciar un **objeto** de dicha clase
6. Crear una **clase** de nombre **Persona** que tenga las propiedades **nombre, apellidos, edad**, e instanciar un **objeto** de dicha clase
7. Crear una **clase** de nombre **Avion** que tenga las propiedades y métodos **numPasajeros, despegar (imprime por consola 'despegando'), volar (imprime por consola 'llegando al destino'), aterrizar (imprime por consola 'aterrizando')**, e instanciar un **objeto** de dicha clase
8. Crear una **clase** de nombre **Paquete** que tenga una **lista con todos los objetos que contenga el paquete**, e instanciar un **objeto** de dicha clase
9. Crear una **clase** de nombre **Pais** que tenga las propiedades **numHabitantes, continente, gentilicio**, e instanciar un **objeto** de dicha clase

### Lectura de propiedades

10. Dado un **objeto** de nombre **Portatil**, obtener el valor de la propiedad **marca con .marca** guardándolo en la variable **marcaPortatil**
11. Dado un **objeto** de nombre **Concierto**, obtener el valor de la propiedad **listaGrupos** guardándolo en la variable **grupos**
12. Dado un **objeto** de nombre **Led**, obtener el valor de las propiedades **rojo, verde y azul** guardándolo en la variable **tuplaRGB(rojo, verde, azul)**
13. Dado un **objeto** de nombre **OhNoError**, obtener el valor de la propiedad **codigo** guardándolo en la variable **codError**
14. Dado un **objeto** de nombre **Grupo** obtener el valor de la propiedad **listaIntegrantes** (de tipo lista) guardándolo en la variable **integrantes**
15. Dado un **objeto** de nombre **Impresora** obtener el valor de la propiedad **tinta** (de tipo diccionario: `{"rojo": 100, "verde": 100, "azul": 100}`) guardándolo en la variable **nivelesTinta**
16. Dado un **objeto** de nombre **Ventana** obtener el valor de la propiedad **dimensiones** (de tipo tupla bidimensional: `((alto, ancho), (posicionX, posicionY))`) guardándolo en la variable **pixeles**

### Modificación de propiedades

17. Dado un **objeto** de nombre **Portatil**, modificar el valor de la propiedad **modelo** por el valor **P345**
18. Dado un **objeto** de nombre **Concierto**, añadir el valor **Guns N' Roses** a la propiedad **cartelera**
19. Dado un **objeto** de nombre **Concierto**, modificar el valor de la propiedad **fecha** por el valor correspondiente a la fecha actual, obtenida automáticamente del sistema
20. Dado un **objeto** de nombre **Impresora**, modificar el valor de la propiedad **imprimiendo** por **un diccionario con los campos: nombreArchivo, copias, numPaginas** (con los valores que se desee)
21. Dado un **objeto** de nombre **Grupo**, modificar el valor de la propiedad **numIntegrantes** por el valor **5**
22. Dado un **objeto** de nombre **Ventana**, modificar el valor de la propiedad **dimensiones** por el valor **((640,480),(120,80))**
23. Dado un **objeto** de nombre **Led**, modificar el valor de la propiedad **encendido** por el valor **false si vale true y true si vale false**
24. Dado un **objeto** de nombre **Movil**, modificar el valor de la propiedad **temperatura** por el valor **20º**