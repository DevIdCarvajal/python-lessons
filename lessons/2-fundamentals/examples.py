# ------------- Conditional -------------

age = input("Escribe tu edad: ")
intAge = int(age)

if(intAge >= 65):
  cost = 10
elif(intAge < 65 and intAge > 17):
  cost = 30
else: # 17 o menos
  cost = 20

print("El precio final es: " + str(cost))

# ------------- Loop -------------

weekend = False # 1

while(weekend == False):
  today = input("¿Qué día es hoy (LMXJVSD)? ")

  if(today == "S" or today == "D"):
    weekend = True # 3

print("Qué bien! Es finde!")

# ------------- Dictionaries -------------

teacher = {
  "name": "David",
  "age": 22,
  "skills": ["Python", "JavaScript", "Poetry"]
}

print("Soy " + teacher["name"] + ", tengo " + str(teacher["age"]) + " años y esto es lo que sé hacer:" )

for skill in teacher["skills"]:
  print(skill)

# ------------- Functions -------------

# Define/Declarate function
def calculator(num1, num2, operation):
  if(operation == "sumar"):
    total = num1 + num2
  elif(operation == "restar"):
    total = num1 - num2
  else:
    total = "Error"
  
  return total

# Call/Invoke function
result = calculator(3, 7, "sumar")
print(result)

result = calculator(3, 7, "restar")
print(result)

result = calculator(3, 7, "alcachofear")
print(result)

# Example w/ lists
def duplicateList(myList):
  result = []

  for elem in myList:
    result.append(elem * 2)

  return result

newList = duplicateList([3, 5])