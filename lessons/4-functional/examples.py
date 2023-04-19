from functools import reduce

numbers = [4, 6, 7, 8]

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

# ----------------------------------

def esPar(num):
  return num % 2 == 0

esParLambda = lambda num: num % 2 == 0

def mayorQue5(num):
  return num > 5

#print(list(filter(esPar, numbers)))
print(list(filter(mayorQue5, numbers)))

# ----------------------------------

# def sigma(total, nextData):
#   return total + nextData

# sigmaL = lambda total, nextData : total + nextData

if(len(numbers) > 0):
  print(reduce(lambda total, nextData : total + nextData, numbers))
else:
  print("Lista vacía")

# ----------------------------------

def mayorQue(limit):
  return lambda num : num > limit

print(list(filter(mayorQue(5), numbers)))
