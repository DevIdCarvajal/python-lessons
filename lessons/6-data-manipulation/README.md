# 6. Manipulación de datos

## Índice

[1. Manejo de JSON](#1-manejo-de-json)  
[2. Librería pandas](#2-librería-pandas)  
[3. Librería matplotlib](#3-librería-matplotlib)

## 1. Manejo de JSON

Para cargar un JSON en un diccionario:

    import json

    x =  '{ "name":"John", "age":30, "city":"New York"}'

    y = json.loads(x)

    print(y["age"])

Para convertir a JSON desde un diccionario:

    import json

    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }

    y = json.dumps(x)

    print(y)

## 2. Librería pandas

.

## 3. Librería matplotlib

.

## Referencias

[JSON](https://www.w3schools.com/python/python_json.asp)  
[Manipulación de datos con pandas](https://www.w3schools.com/python/pandas/default.asp)  
[Visualización de datos con matplotlib](https://www.w3schools.com/python/matplotlib_intro.asp)  
[La librería Pandas](https://aprendeconalf.es/docencia/python/manual/pandas/)  
[La librería Matplotlib](https://aprendeconalf.es/docencia/python/manual/matplotlib/)