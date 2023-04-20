# 3. Programación orientada a objetos

## Índice

[1. Fundamentos de la POO](#1-fundamentos-de-la-poo)  
[2. Clases](#2-clases)   
[3. Métodos especiales](#3-métodos-especiales)

## 1. Fundamentos de la POO

- Abstracción
- Encapsulamiento
- Modularidad
- Herencia
- Polimorfismo

## 2. Clases

Esto es una clase, de la que se pueden instanciar objetos:

    class Horse:
      alive = True

      def __init__(self, name = '', speed = 10):
        self.name = name
        self.speed = speed

      def run(self):
        if self.alive:
          self.speed += 5

          if self.speed > 50:
            self.alive = False
        else:
          print('No puedo más')

      def brake(self):
        self.speed -= 5

      def say(self, something):
        print(something)

    caballoNormal = Horse()
    caballoNormal.speed = 25
    print(f"{caballoNormal.name}, {caballoNormal.speed}")

    yeguaRapida = Horse(speed = 20)
    print(f"{yeguaRapida.name}, {yeguaRapida.speed}")

    laDelCid = Horse("Babieca", 15)
    laDelCid.run()
    laDelCid.say("Ou yeah")

Una clase puede heredar de otra, redefiniendo o añadiendo propiedades y/o métodos:

    class Meara(Horse):
      def __init__(self, name = '', speed = 30):
        super().__init__(name, speed)
        self.country = 'Rohan'
      def beMagic(self):
        print('Soy increíble')

    elDeGandalf = Meara(name = "Sombragrís")
    print(f"{elDeGandalf.name}, {elDeGandalf.speed}, {elDeGandalf.country}")

## 3. Métodos especiales

Además del constructor, en Python existen otros métodos especiales para sobrecargar otros "métodos mágicos" u operadores por defecto:

    class MagnifiedList:
      def __init__(self, normalList):
        self.data = normalList
      def __len__(self):
        return len(self.data) + 2

    myList = MagnifiedList([1, 2, 3])
    print(len(myList))

## Referencias

[Programación orientada a objetos](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos)  
[Clases](https://www.w3schools.com/python/python_classes.asp)  
[Herencia](https://www.w3schools.com/python/python_inheritance.asp)  
[Métodos especiales](https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html)