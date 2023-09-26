# 1. Introducción

## Índice

[1. Definición y características](#1-definición-y-características)  
[2. Instalación](#2-instalación)  
[3. Hola Mundo](#3-hola-mundo)  
[4. Gestión de paquetes](#4-gestión-de-paquetes)

## 1. Definición y características

- Python es un lenguaje de programación completo (control de flujo, funciones, etc.) enfocado a la legibilidad.
- Interpretado con tipado dinámico fuerte.
- Multiplataforma, gratuito y de propósito general.
- Tiene una comunidad y un ecosistema de código abierto (librerías y paquetes) muy potente.
- Se llama así porque su creador era fan de los Monty Python.

## 2. Instalación

- Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Extensión de Python para VS Code: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 3. Hola Mundo

1. Abrir Visual Studio Code
2. Crear un fichero nuevo: File > New File ( `Ctrl + N` )
3. Añadir estas dos líneas:

        msg = "Hello World"
        print(msg)

4. Guardarlo con el nombre `hello.py`
5. Ejecutar fichero en la terminal:

- Windows:

      python hello.py

- Mac/Linux:

      python3 hello.py

## 3. Gestión de paquetes

Para instalar nuevos paquetes, puede hacerse desde la terminal mediante el gestor de paquetes de Python, conocido como `pip`, de esta forma:

    pip install pandas

Para ver los paquetes instalados actualmente:

    pip list

Para desinstalar un paquete:

    pip uninstall pandas

## Referencias

[Python: qué es, para qué sirve y cómo se programa](https://www.cursosaula21.com/que-es-python/)
[Documentación oficial de VS Code](https://code.visualstudio.com/docs/python/python-tutorial)