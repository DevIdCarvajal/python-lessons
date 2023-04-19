# 1. Primeros pasos con Python

## Índice

[0. Prerrequisitos](#0-prerrequisitos)  
[1. Nuestra primera aplicación Python: "Hola Mundo"](#1-nuestra-primera-aplicación-python-"hola-mundo")  
[2. Instalar paquetes (con entornos virtuales)](#2-instalar-paquetes-con-entornos-virtuales)

## 0. Prerrequisitos

- Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Extensión de Python para VS Code: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Git: [https://git-scm.com/download/](https://git-scm.com/download/)

## 1. Nuestra primera aplicación Python: "Hola Mundo"

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

## 2. Instalar paquetes (con entornos virtuales)

1. Crear un fichero `standardplot.py`

2. Añadir estas líneas:
   
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(0, 20, 100)
        plt.plot(x, np.sin(x))
        plt.show()

3. Ejecutar y depurar el script (error de dependencias)

4. Crear y activar el entorno virtual

- Windows:
  
      py -3 -m venv .venv
      .venv\scripts\activate

    En caso del error:

    "Activate.ps1 is not digitally signed. You cannot run this script on the current system."

    Introducir esto en la PowerShell:

      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

- Mac/Linux:

      python3 -m venv .venv
      source .venv/bin/activate

1. Seleccionar el entorno virtual

    (Ctrl+Shift+P > Python: Select Interpreter)

2. Instalar los paquetes:

- Windows:
  
      python -m pip install matplotlib

- Mac:

      python3 -m pip install matplotlib

- Linux:

      apt-get install python3-tk
      python3 -m pip install matplotlib

## Referencias

[Documentación oficial de VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages)  
[Entornos virtuales con Python](https://code.tutsplus.com/es/tutorials/understanding-virtual-environments-in-python--cms-28272)