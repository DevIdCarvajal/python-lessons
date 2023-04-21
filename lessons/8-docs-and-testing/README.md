# 8. Documentación y pruebas unitarias

## Índice

[1. Documentación](#1-documentación)  
[2. Pruebas unitarias](#2-pruebas-unitarias)

## 1. Documentación

El código Python se puede documentar fácilmente mediante Docstrings:

    def square(a):
      '''Returned argument a is squared.'''
      return a**a

    print(square.__doc__)

    help(square)

O se puede utilizar el paquete Sphinx.

## 2. Pruebas unitarias

Entre las distintas fases del desarrollo de un proyecto software, existe una conocida como la fase de pruebas, que se encarga de tratar de asegurar unos mínimos de calidad del software implementado.

Existen muchos tipos de pruebas, entre ellas las conocidas como unitarias (unit tests), enmarcados dentro de la metodología TDD (Test-Driven Development, o Desarrollo Guiado por Pruebas).

![](tdd.jpg)

Esta metodología trata de enfocar el desarrollo hacia la superación de pruebas individuales para todos (o la mayoría de) los tipos de casos particulares que pueden darse al llamar a una función.

El flujo de trabajo determina empezar por escribir el test, fallido desde el principio; después escribir el código que lo pasa; finalmente la refactorización de dicho código y vuelta a empezar con el siguiente test.

La librería `doctest` sirve para realizar pruebas unitarias de funciones fácilmente, expresándolas en forma de documentación (mediante comentarios):

    import doctest

    def totalSumDouble(*args):
      """
      Devuelve la suma del doble de todos sus parámetros

      Pruebas a realizar
      (entrada determinada y salida esperada):

      >>> totalSumDouble(1, 2, 3)
      12
      
      >>> totalSumDouble(-10, 15)
      0
      """
      return sum(args * 2)
    
    doctest.testmod(name='totalSumDouble', verbose=True)

De esta forma, en un bloque de comentarios, se usa el prefijo `>>>` para indicar el código del test, y justo debajo la salida esperada.

El siguiente es un ejemplo en el que los tests van "guiando" el desarrollo (aplicando TDD):

    import doctest

    def palindrome(word):
      """
      Devuelve True si la palabra pasada por parámetro
      es un palíndromo y False en caso contrario

      >>> palindrome("radar")
      True

      >>> palindrome("tractor")
      False
      
      >>> palindrome("Ada")
      True
      """
      if word == word[::-1]:
        return True
      else:
        return False
      
      doctest.testmod(name='palindrome', verbose=True)

El test falla, porque es sensible a mayúsculas (*case sensitive*), cuando no debería serlo, así que puede modificarse el condicional por este otro:

    if word.lower() == word[::-1].lower():

Si añadimos un test que tiene espacios, también falla, cuando no debería:

    >>> palindrome("A dama amada")
    True

Lo que implica ajustar el código para que pase el test (sin dejar de pasar el resto):

    if word.lower().replace(" ", "") ==
      word[::-1].lower().replace(" ", ""):

Y así sucesivamente para todos los casos que se deseen contemplar (tildes, etc.).

Otra opción es utilizar el paquete Pytest.

## Referencias

[Tutorial de docstrings](https://www.programiz.com/python-programming/docstrings)  
[Tutorial de Sphinx](https://medium.com/qu4nt/documentaci%C3%B3n-con-sphinx-y-python-9a777403cb68)  
[Documentación Sphinx](https://www.sphinx-doc.org/en/master/)

[Pruebas unitarias con doctest](https://docs.hektorprofe.net/python/documentacion-y-pruebas/doctest/)  
[Metodología TDD](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/que-es-el-test-driven-development/)  
[Pytest](https://tutoriales.edu.lat/pub/pytest/pytest-quick-guide/pytest-guia-rapida)