# 4. Programación funcional

## Índice

[1. Funciones de orden superior](#1-funciones-de-orden-superior)  
[2. Iteraciones de orden superior sobre listas](#2-iteraciones-de-orden-superior-sobre-listas)  
[3. Funciones lambda](#3-funciones-lambda)  
[4. Comprensión de listas](#4-comprensión-de-listas)  
[5. Generadores](#5-generadores)  
[6. Decoradores](#6-decoradores)

## 1. Funciones de orden superior

Son funciones que pueden recibir como parámetros otras funciones y/o devolverlas como resultados:

    def calculate(valor1, valor2, operatorFunction):
      return operatorFunction(valor1, valor2)

    def add(x1, x2):
      return x1 + x2

    def substract(x1, x2):
      return x1 - x2

    def multiply(x1, x2):
      return x1 * x2

    def divide(x1, x2):
      return x1 / x2

    number1 = 10
    number2 = 3

    print(f"{number1} + {number2} vale {calculate(number1, number2, add)}")
    print(f"{number1} - {number2} vale {calculate(number1, number2, substract)}")
    print(f"{number1} x {number2} vale {calculate(number1, number2, multiply)}")
    print(f"{number1} / {number2} vale {calculate(number1, number2, divide)}")

Y con clases quedaría de este modo:

    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def isAdult(self, checkFunction):
        return checkFunction(self.age)

    def adultUSA(age):
      if age >= 21:
        return True
      else:
        return False

    def adultSpain(age):
      if age >= 18:
        return True
      else:
        return False

    bicentennialMan = Person("Andrew", 20)

    if bicentennialMan.isAdult(adultSpain):
      print(f"{bicentennialMan.name} es mayor de edad si vive en España")
    else:
      print(f"{bicentennialMan.name} no es mayor de edad si vive en España")

    if bicentennialMan.isAdult(adultUSA):
      print(f"{bicentennialMan.name} es mayor de edad si vive en Estados Unidos")
    else:
      print(f"{bicentennialMan.name} no es mayor de edad si vive en Estados Unidos")

## 2. Iteraciones de orden superior sobre listas

Es posible iterar listas aplicando funciones en cada iteración mediante las funciones específicas ya definidas map(), filter() y reduce().

En primer lugar está map, que sirve para aplicar una función a todos los elementos de una lista y devolver un nuevo objeto iterable con los elementos resultantes:

    def startsWithA(string):
      return string[0] == "A"

    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    mapObject = map(startsWithA, fruits)

    print(list(mapObject))

Después está filter, que sirve para, dada una función que devuelve una expresión de comparación lógica y una lista, aplica la condición determinada por la función a todos los elementos de la lista, y devuelve un nuevo objeto iterable con los elementos filtrados por dicha condición:

    def endsWithE(string):
      return string[-1] == "e"

    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    filterObject = filter(endsWithE, fruits)

    print(list(filterObject))

Por último tenemos reduce, que dada una función acumuladora y una lista, aplica el resultado de ir recorriendo los elementos de la lista, acumulando el resultado generado por la función, y devuelve el valor resultante de la acumulación:

    from functools import reduce

    def sigma(x, y):
      return x + y

    list = [2, 4, 7, 3]
    print(reduce(sigma, list))

En el caso de reduce, opcionalmente es posible también establecer un valor inicial antes de empezar la acumulación, que también se procesará con el primer elemento de la lista:

    print(reduce(sigma, list, 10))

## 3. Funciones lambda

Son funciones anónimas definidas "en una línea", es decir, de una sola expresión que normalmente se emplean en casos en los que se necesita un cálculo puntual por un breve periodo de tiempo.

Siguiendo las técnicas del paradigma de la programación funcional, los casos habituales de uso de las funciones lambda serían:

- Almacenarlas en una variable en caso de querer ser reutilizadas:

      levelUp = lambda level : level + 1
      print(levelUp(8))

      concatenateWithColon = lambda string1, string2 : f"{string1}:{string2}"
      print(concatenateWithColon(4,7))

- Pasarlas como parámetros a otras funciones como "callbacks":

      def calculateWithLambda(valor1, valor2, operatorFunction):
        return operatorFunction(valor1, valor2)

      print(calculateWithLambda(10, 3, lambda x1, x2 : x1 + x2))

- Devolverlas como valor de retorno de otras funciones ("currificación"):

      def multiplier(n):
        return lambda number : number * n

      duplicater = multiplier(2)
      triplicater = multiplier(3)

      print(duplicater(111))
      print(triplicater(111))

      # Currying version

      print(multiplier(4)(111))
      print(multiplier(5)(111))

## 4. Comprensión de listas

Se trata de una forma abreviada de generar una nueva lista a partir del procesamiento de otra lista previa. Realmente es lo mismo que las iteraciones de orden superior sobre listas, solo que con una sintaxis más ligera.

Lo que haríamos mediante un bucle for de esta manera:

    skills = ["design", "maths", "poetry", "coding", "macramé"]
    skillsWithO = []

    for skill in skills:
      if "o" in skill:
        skillsWithO.append(skill)

    print(skillsWithO)

Lo podemos hacer con la técnica de comprensión de listas de esta otra:

    skills = ["design", "maths", "poetry", "coding", "macramé"]

    skillsWithO = [skill for skill in skills if "o" in skill]

    print(skillsWithO)

El condicional que se pone al final (totalmente opcional si no se desea), detrás del bucle, actúa como filtrador de los elementos que se incluirán en la nueva lista resultado.

Además, es posible también usar expresiones para manipular los elementos una vez filtrados, de manera que se almacenen subproductos de los mismos:

    # Option 1
    skillsWithO = [skill.upper() for skill in skills if "o" in skill]

    # Option 2
    skillsWithO = [skill if skill != "coding" else "programming" for skill in skills]

## 5. Generadores

Son funciones capaces de generar un sinfín de resultados obtenidos "poco a poco", es decir, en pasos sucesivos y en tiempo de ejecución, lo que implica un menor coste de recursos:

    def getEven():
      index = 1
      
      # ¡Atención, bucle infinito!
      while True:
          
        # Devolvemos un valor
        yield index * 2
        index = index + 1

    for i in getEven():
      print(i)

## 6. Decoradores

Se trata de un patrón de diseño que consiste en una función que recibe otra función, la extiende (dotándola de mayor funcionalidad) y la devuelve:

    def sayHelloDecorator(decoratedFunction):
      def giveSuperPowers():
        print("Hello")
        decoratedFunction()
        print("Bye")
      return giveSuperPowers

    def printAdaName():
      print("Ada")

    printAdaName = sayHelloDecorator(printAdaName)
    printAdaName()

Versión simplificada (notación @):

    def sayHelloDecorator(decoratedFunction):
      def giveSuperPowers():
        print("Hello")
        decoratedFunction()
        print("Bye")
      return giveSuperPowers

    @sayHelloDecorator
    def printAdaName():
      print("Ada")

    printAdaName()

## Referencias

[Funciones de orden superior I](https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?codigo=93)  
[Funciones de orden superior II (filter, map y lambda)](https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_orden_superior.html)  
[map(), filter() y reduce()](https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/)  
[Funciones lambda](https://www.w3schools.com/python/python_lambda.asp)  
[Comprensión de listas](https://www.w3schools.com/python/python_lists_comprehension.asp)  
[Currificación](https://www.campusmvp.es/recursos/post/Que-es-la-Currificacion-en-programacion-funcional.aspx)  
[Generadores](https://python-intermedio.readthedocs.io/es/latest/generators.html)  
[Decoradores](https://python-intermedio.readthedocs.io/es/latest/decorators.html)  
[Generador Fibonacci](https://www.csestack.org/python-fibonacci-generator/)