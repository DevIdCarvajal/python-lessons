# 2. Fundamentos de programación en Python

## Índice

[1. Variables, tipos de datos y operadores](#1-variables-tipos-de-datos-y-operadores)  
[2. Listas, tuplas y diccionarios](#2-listas-tuplas-y-diccionarios)  
[3. Condicionales y bucles](#3-condicionales-y-bucles)  
[4. Funciones](#4-funciones)

## 1. Variables, tipos de datos y operadores

Esto son (asignaciones de) variables:

```
name = 'Espagueti'
lastname = "Volador"
age = 16
```

Podemos mostrar su valor:

```
print(name)
```

Y su tipo:

```
print(type(name))
```

Python presenta todos estos tipos:

```
String - str
Integer - int
Float - float
Complex - complex
Boolean - bool
List - list
Tuple - tuple
Set - set
Dictionary - dict
None
```

Podemos capturar un valor y asignárselo:

```
name = input("Escribe tu nombre: ")
print(name)
```

Convertirlo (casting):

```
age = int(input("Escribe tu edad: "))
print(age)
```

Si es un string, concatenar varios:

```
# - Con el operador:
print("Hola, " + name + " " + lastname + ", tienes " + age + " años")

# - Con la notación f-string:
print(f"Adiós, {name} {lastname}, tienes {age} años")
```

## 2. Listas, tuplas y diccionarios

### Listas

Esto son ejemplos de listas:

```
colors = ["red", "blue", "green"]
stuff = ["thing", 3, True]
```

Se accede por su índice numérico (empieza en cero, acaba en menos uno):

```
print(colors[0])
print(colors[-1])
```

Se pueden añadir y eliminar elementos:

```
colors.remove("blue")
colors.append("orange")
print(colors)
```

Se pueden recorrer:

```
for color in colors:
    print(color)
```

### Tuplas

Esto es un ejemplo de tupla:

```
position = (2, 3, -1)
```

Las tuplas no se pueden modificar parcialmente, pero sí totalmente:

```
position.remove(2) # Error
```

### Diccionarios

Esto son ejemplos de diccionarios:

```
dictionary = {1:"X", "X":2}
godness = {"name": 'Unicornio', "lastname": 'Rosa Invisible', 'age': 31}
```

Se accede por su clave:

```
print(dictionary[1])
print(godness["name"])
```

Se pueden añadir y eliminar elementos:

```
godness["place"] = "rainbow"
print(godness)

godness.pop("place")
print(godness)

# Otra opción para borrar:
# del godness["place"]
```

Se pueden recorrer:

```
# Claves:

for key in godness:
    print(key)

# Otra forma:

for key in thisdict.keys():
    print(key)

# Valores:

for value in godness:
    print(godness[value])

# Otra forma:

for value in godness.values():
    print(value)

# Claves y valores:

for key, value in godness.items():
    print(key, value)
```

## 3. Condicionales y bucles

Para las estructuras de control de flujo se usan operadores de comparación y operadores lógicos:

```
== != < <= > >=
and or not
```

### Condicionales

```
a = 1
b = 2
if b > a:
    print("b es mayor que a")
```

Puede haber condicionales de dos o más ramas:

```
a = 1
b = 2
c = 3
if a > b:
    print("a es mayor que b")
else:
    print("b es mayor que a")

if a > c:
    print("a es mayor que c")
elif a > b:
    print("a es mayor que b")
else:
    print("a es el más pequeño de todos")
```

### Bucles

Un bucle debe tener tres elementos:

- Inicialización previa
- Condición de parada
- Cambios en cada iteración

```
## While

i = 0

while i < 5:
    print(i)
    i += 1

## For .. in

for i in range(5):
    print(i)

for letter in "abracadabra":
    print(letter)

```

## 4. Funciones

Una función se define de la siguiente manera:

```
def learn():
    print("¡Estoy aprendiendo Python!")
```

Y se la llama así:

```
learn()
```

Puede recibir argumentos:

```
def learn(subject):
    print(f"¡Estoy aprendiendo {subject}!")
```

Puede devolver valores:

```
def learnMore(subject, level):
    print (f"¡Estoy aprendiendo {subject}!")

    return level + 1

level = 0
level = learnMore(subject, level)
```

¡Cuidado con el ámbito (local vs global)!

## Referencias

[Variables](https://www.w3schools.com/python/python_variables.asp)  
[Tipos de datos](https://www.w3schools.com/python/python_variables.asp)  
[Operadores](https://www.w3schools.com/python/python_operators.asp)  
[Listas](https://www.w3schools.com/python/python_lists.asp)  
[Tuplas](https://www.w3schools.com/python/python_tuples.asp)  
[Diccionarios](https://www.w3schools.com/python/python_dictionaries.asp)  
[Condicionales](https://www.w3schools.com/python/python_conditions.asp)  
[Bucles While](https://www.w3schools.com/python/python_while_loops.asp)  
[Bucles For](https://www.w3schools.com/python/python_for_loops.asp)  
[Funciones](https://www.w3schools.com/python/python_functions.asp)  
[Ámbito](https://www.w3schools.com/python/python_scope.asp)

[Python Tutor](https://pythontutor.com/)
