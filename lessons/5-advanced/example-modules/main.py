#import calculatorF # F1
from calculatorF import add # F2

#print(calculatorF.add(1, 2)) # F1
print(add(1, 2)) # F2

# ------------------------------------------

import calculatorOO # OO1
#from calculatorOO import Calculator # OO2

myCalculator = calculatorOO.Calculator() # OO1
#myCalculator = Calculator() # OO2

print(myCalculator.add(1, 2))

# ------------------------------------------

import random

# Número aleatorio de 0 a 10 incluidos
print(random.randrange(0, 11))
