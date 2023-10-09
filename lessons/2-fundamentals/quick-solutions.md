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

    booleanoMix1 = (booleano1 and (TAU[0]/2 == PI[0] and TAU[1]/2 == PI[1])) or (variableValorNumerico >= miNumeroFav)

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

    contarHasta10while = 0
    
    while(contarHasta10while < 10):
      contarHasta10while += 1

20

    i = 0
    j = 0

    while(i < 11):
      j += i**2
      i += 1

21

    sumaPares = 0
    i = 0

    while(i < 10):
      if(i % 2 == 0):
        sumaPares += i
      i += 1

22

    contarHasta10for = 0

    for x in range(10):
      contarHasta10for += 1
