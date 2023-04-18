# Soluciones rápidas

1

    # Option 1
    variableSinValor = None

    # Option 2
    variableSinValor = ""

2

    booleano1 = True
    booleano2 = False

3

    PI = (3,14)

4

    TAU = (PI[0]*2, PI[1]*2)

5

    variableValorNumerico = 42

6

    miNombre = "Ripley"

7

    miNumeroFav = 3.15

8

    booleanoAnd = booleano1 and booleano2

9

    booleanoNot = not booleano1

10

    booleanoMix0 = (booleano1 or booleano2) and (booleano1 or (not booleano1 and not booleano2)

11

    booleanoOr = booleano1 or booleano2

12

    booleanoMix1 = (booleano1 and (TAU/2 == PI)) or (variableValorNumerico >= miNumeroFav)

13

    seisNoEsNueve = 6 != 9

14

    formateadoTAU = float(TAU[0]) + float(TAU[1]) / 100

    booleanoMix2 = (variableValorNumerico > 0) or (variableValorNumerico < -(miNumeroFav * formateadoTAU))

15

    valorSuma = miNumeroFav + variableValorNumerico

16

    valorResta = miNumeroFav - variableValorNumerico

17

    valorMultiplicacion = miNumeroFav * variableValorNumerico

18

    valorDivision = miNumeroFav / 3

19

    listaVacia = []

20

    # Option 1
    listaNumeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Option 2
    listaNumeros = [] 
    for x in range(10):
      listaNumeros.append(x)

21

    # Option 1
    listaNumerosPares = [0, 2, 4, 6, 8]
    
    # Option 2
    listaNumerosPares = [] 
    for x in range(10):
      if(x % 2 == 0):
        listaNumerosPares.append(x)

22

    listaBidimensional = [[0, 1, 2], ['a', 'b', 'c']]

23

    contarHasta10while = 0
    
    while(contarHasta10while < 10):
      contarHasta10while += 1

24

    i = 0
    j = 0

    while(i < 11):
      j += i**2
      i += 1

25

    sumaPares = 0
    i = 0

    while(i < 10):
      if(i % 2 == 0):
        sumaPares += i
      i += 1

26

    contarHasta10for = 0

    for x in range(10):
      contarHasta10for += 1

27

    def suma(num1, num2):
      return num1 + num2

28

    def potenciacion(num1, num2):
      return num1**num2

29

    def separarPalabras(palabra):
      return palabra.split()

30

    def repetirString(palabra, num):
      result = ""
      for x in range(num):
        result += palabra
      return result

31

    def esPrimo(num):
      if(num >= 42):
        return False
      
      for i in range(2, num):
        if (num % i) == 0:
          return False
      
      return True

32

    def multiplicacion(num1, num2):
      return num1 * num2

33

    def division(num1, num2):
      return num1 / num2

34

    def esPar(num):
      return num % 2 == 0

35

    def ordenarLista(lista):
      return lista.sort()

36

    def obtenerPares(lista):
      listaPares = []

      for x in lista:
        if(x % 2 == 0):
          listaPares.append(x)
      
      return listaPares

37

    def pintarLista(lista):
      return str(lista)

38

    def eliminarDuplicados(lista):
      return list(dict.fromkeys(lista))

39

    def ordenarLista2(lista):
      return lista.sort(reverse = True)

40

    def obtenerImpares(lista):
      listaImpares = []

      for x in lista:
        if(x % 2 != 0):
          listaImpares.append(x)
      
      return listaImpares

41

    def sumarLista(lista):
      total = 0

      for x in lista:
        total += x
      
      return total

42

    multiplicarLista(lista):
      total = 1

      for x in lista:
        total *= x
      
      return total

43

    def multiplicacionPro(num1, num2):
      total = 0

      for x in range(num2):
        total += num1
      
      return total
