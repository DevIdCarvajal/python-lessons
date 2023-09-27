# Soluciones rápidas

1

    listaVacia = []

2

    # Option 1
    listaNumeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Option 2
    listaNumeros = [] 
    for x in range(10):
      listaNumeros.append(x)

3

    # Option 1
    listaNumerosPares = [0, 2, 4, 6, 8]
    
    # Option 2
    listaNumerosPares = [] 
    for x in range(10):
      if(x % 2 == 0):
        listaNumerosPares.append(x)

4

    listaBidimensional = [[0, 1, 2], ['a', 'b', 'c']]