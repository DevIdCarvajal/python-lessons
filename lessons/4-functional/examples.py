# ------------- Map, filter, reduce -------------

numbers = [4, 6, 7, 8]

# -- Map

# Non-functional approach
numbersD = []

for x in numbers:
  numbersD.append(x*2)

print(numbersD)

# Functional approach
def duplicate(num):
  return num * 2

mapObject = map(duplicate, numbers)
#mapObject = map(lambda num: num * 2, numbers)

print(list(mapObject))

# -- Filter

def esPar(num):
  return num % 2 == 0

esParLambda = lambda num: num % 2 == 0

def mayorQue5(num):
  return num > 5

print(list(filter(esPar, numbers)))
print(list(filter(mayorQue5, numbers)))

# -- Reduce

from functools import reduce

def sigma(total, nextData):
  return total + nextData

sigmaL = lambda total, nextData : total + nextData

if(len(numbers) > 0):
  #print(reduce(sigma, numbers))
  #print(reduce(sigmaL, numbers))
  print(reduce(lambda total, nextData : total + nextData, numbers))
else:
  print("Lista vacía")

# ------------- Currying -------------

def mayorQue(limit):
  return lambda num : num > limit

print(list(filter(mayorQue(2), numbers)))

def entre(limitInf, limitSup):
  return lambda num : limitInf < num and num < limitSup

print(list(filter(entre(2, 8), numbers)))
print(entre(6,14)(8))

# ------------- Generators -------------

def fibonacciGen(limit):
  a=0
  b=1
  
  for i in range(limit):
    yield b
    a, b = b, a+b

obj = fibonacciGen(100)
r = ""

while r != "Q":
  r = input("Quieres otro? (Q para salir)")

  print(next(obj))

# ------------- Decorators -------------

def sayHelloDecorator(decoratedFunction):

  def giveSuperPowers():
    print("Hello")

    decoratedFunction()

    print("Bye")
  
  return giveSuperPowers

@sayHelloDecorator
def printAdaName():
  print("Ada")

@sayHelloDecorator
def doSomething():
  for i in range(3):
    print(i)

printAdaName()
doSomething()