# Soluciones rápidas

1

    def suma(num1, num2):
      return num1 + num2

2

    def potenciacion(num1, num2):
      return num1**num2

3

    def separarPalabras(palabra):
      return palabra.split()

4

    def repetirString(palabra, num):
      result = ""
      for x in range(num):
        result += palabra
      return result

5

    def esPrimo(num):
      if(num >= 42):
        return False
      
      for i in range(2, num):
        if (num % i) == 0:
          return False
      
      return True

6

    def multiplicacion(num1, num2):
      return num1 * num2

7

    def division(num1, num2):
      return num1 / num2

8

    def esPar(num):
      return num % 2 == 0

9

    def ordenarLista(lista):
      return lista.sort()

10

    def obtenerPares(lista):
      listaPares = []

      for x in lista:
        if(x % 2 == 0):
          listaPares.append(x)
      
      return listaPares

11

    def pintarLista(lista):
      return str(lista)

12

    def eliminarDuplicados(lista):
      return list(dict.fromkeys(lista))

13

    def ordenarLista2(lista):
      return lista.sort(reverse = True)

14

    def obtenerImpares(lista):
      listaImpares = []

      for x in lista:
        if(x % 2 != 0):
          listaImpares.append(x)
      
      return listaImpares

15

    def sumarLista(lista):
      total = 0

      for x in lista:
        total += x
      
      return total

16

    multiplicarLista(lista):
      total = 1

      for x in lista:
        total *= x
      
      return total

17

    def multiplicacionPro(num1, num2):
      total = 0

      for x in range(num2):
        total += num1
      
      return total