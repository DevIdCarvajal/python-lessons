# ------------- Class -------------

class Calculator:

  # Constructor
  def __init__(self, extra, model):

    # Properties
    self.extra = extra
    self.model = model
    self.energy = 3

  # Methods
  def add(self, num1, num2):
    if(self.energy > 0):

      self.energy -= 1
      total = num1 + num2

      return total
    else:
      return "Error"
  
  def substract(self, num1, num2):
    if(self.energy > 0):

      self.energy -= 1
      total = num2 - num1

      return total
    else:
      return "Error"

# Instantiation
myCalculator = Calculator(False, "Casio XR-43")
print( myCalculator.add( 3, 4 ) )
print( myCalculator.add( 13, 14 ) )
print( myCalculator.substract( 6, 4 ) )
print( myCalculator.substract( 9, 6 ) )

myCalculatorPro = Calculator(True, "HP 78fr")
print( myCalculatorPro.add(3, 5) )

# ------------- Inheritance -------------

# Base class / Superclass
class Human:
  def __init__(self, age, name, surname):
    self.age = age
    self.name = name
    self.surname = surname

    self.language = "en"

    self.adult = self.iAmAdult(age)
    # if( self.iAmAdult(age) ):
    #   self.adult = True
    # else:
    #   self.adult = False
  
  def grow(self):
    self.age += 1

    self.adult = self.iAmAdult(self.age)
  
  def speak(self):
    return "Good morning"
  
  def iAmAdult(self, age):
    if(age >= 18):
      return True
    else:
      return False

# Derived class / Subclass
class Spanish(Human):
  def __init__(self, age, name, surname):
    super().__init__(age, name, surname)

    # Override
    self.language = "es"

  # Override (redefinir)
  def speak(self):
    return "Buenos días"
  
  # Extends (ampliar)
  def code(self):
    return "Aquí tienes tu programa"

human1 = Human(32)
# print(human1.speak())
human1.grow()
print(human1.age)

human2 = Spanish(24)
# print(human2.code())
human2.grow()
print(human2.age)

human3 = Human(17, "Matusalen", "El Sabio")
print(human3.adult)

human3.grow()
print(human3.adult)

# ------------- Polymorphism -------------

userType = input("¿De dónde eres (es/x)?")

userData = {
  "age": 19,
  "name": "Ada",
  "surname": "Lovelace"
}

if(userType == "es"):
  theUser = Spanish(userData["age"], userData["name"], userData["surname"])
else:
  theUser = Human(userData["age"], userData["name"], userData["surname"])

print( type(theUser) ) # Spanish / Human ????
print(theUser.speak()) # Good morning / Buenos días ????
print(theUser.code()) # Error / O no ????
