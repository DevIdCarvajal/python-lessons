from os.path import exists

def writeFile():
  try:
    if exists("dummy.txt"):
      myFile = open("dummy.txt", "a")
    else:
      myFile = open("dummy.txt", "x")

    next = ""

    while next != ".quit":
      next = input("Escribe lo siguiente (.quit para salir): ")

      if next != ".quit":
        myFile.write(next + "\r\n")
  except:
    print("Problemas")
  finally:
    myFile.close()

def readFile():
  if exists("dummy.txt"):
    try:
      myFile = open("dummy.txt", "r")

      next = myFile.readline()

      while next:
        print(next)

        next = myFile.readline()

      return True
    except:
      print("Problemas")

      return False
    finally:
      myFile.close()
  else:
    return False

mode = input("¿Quieres escribir (w) o leer (r)? ")

if mode == "w":
  writeFile()
else:
  if not readFile():
    print("El fichero no existe o no se puede leer")