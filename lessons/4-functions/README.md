
## 4. Funciones

Una función se define de la siguiente manera:

    def learn():
      print("¡Estoy aprendiendo Python!")

Y se la llama así:

    learn()

Puede recibir argumentos:

    def learn(subject):
      print(f"¡Estoy aprendiendo {subject}!")

Puede devolver valores:

    def learnMore(subject, level):
      print (f"¡Estoy aprendiendo {subject}!")

      return level + 1

    level = 0
    level = learnMore(subject, level)

¡Cuidado con el ámbito (local vs global)!


[Funciones](https://www.w3schools.com/python/python_functions.asp)  
[Ámbito](https://www.w3schools.com/python/python_scope.asp)