# 1. Primeros pasos con Python

## Índice

[0. Prerrequisitos](#0-prerrequisitos)  
[1. Hola Mundo](#1-hola-mundo)  
[2. Entornos virtuales](#2-entornos-virtuales)  
[3. Gestión de paquetes](#3-gestión-de-paquetes)

## 0. Prerrequisitos

- Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Extensión de Python para VS Code: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Git: [https://git-scm.com/download/](https://git-scm.com/download/)

## 1. Hola Mundo

1. Crear un fichero `hello.py`
2. Añadir estas dos líneas:

        msg = "Hello World"
        print(msg)

3. Ejecutar fichero en la terminal:

- Windows:

      python hello.py

- Mac/Linux:

      python3 hello.py

1. Depurar el fichero (en VS Code):

   - Punto de parada (F9)
   - Modo de depuración (F5)
   - Consola de depuración

## 2. Entornos virtuales

Se pueden crear fácilmente instancias secundarias del intérprete de Python de manera que estas tengan su propio contexto, independientemente de la instancia principal.

Estas instancias son conocidas como entornos virtuales, y actúan como contenedores aislados y encapsulados, permitiendo generar así entornos seguros de pruebas, sin "ensuciar" el entorno principal.

Para gestionar y trabajar con entornos virtuales, se puede utilizar el paquete `virtualenv`, que se instala con `pip`:

    pip install virtualenv

  - Crear entorno:
  
        virtualenv my-env

  - Activar entorno:
  
        source my-env/bin/activate

  - Desactivar entorno:
  
        deactivate

Para el caso de Visual Studio Code, se debe seleccionar el entorno virtual en el que se va a trabajar, pulsando `Ctrl+Shift+P` y después seleccionando `Python: Select Interpreter`.

## 3. Gestión de paquetes

El gestor de paquetes de Python, conocido como `pip`, es dependiente del entorno, de manera que los paquetes instalados en un entorno no afectan al de otro.

Esto, entre otras ventajas, tiene por ejemplo la de que permite desarrollar aplicaciones que trabajen con distintas versiones de intérpretes o de módulos.

Una vez creado y activado un entorno, podemos instalar paquetes:

    pip install matplotlib

Listar paquetes instalados:

    pip list matplotlib

Desinstalar paquetes:

    pip uninstall matplotlib

Buscar paquetes:

    pip search requests

Crear un fichero con la lista de paquetes instalados y sus versiones actuales:

    pip freeze > requirements.txt

Que se puede reutilizar para instalar rápidamente esos mismos paquetes en otro entorno:

    pip install -r requirements.txt

## Referencias

[Documentación oficial de VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages)  
[Entornos virtuales con Python (I)](https://openwebinars.net/blog/entornos-de-desarrollo-virtuales-con-python3/)  
[Entornos virtuales con Python (II)](https://code.tutsplus.com/es/tutorials/understanding-virtual-environments-in-python--cms-28272)