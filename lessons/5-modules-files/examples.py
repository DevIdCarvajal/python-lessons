# ------------- Files -------------

# Create
f = open("./data/Lorem.txt", "x")
f.close()

# Write
f = open("./data/Lorem.txt", "w")
f.write("Nueva línea 1\n")
f.write("Nueva línea 2\n")
f.close()

# Append
f = open("./data/Lorem.txt", "a")
f.write("Nueva línea 3\n")
f.write("Nueva línea 4\n")
f.close()

# Read
f = open("./data/Lorem.txt", "r")
print(f.read())
f.close()

f = open("./data/Lorem.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# ------------- Serialization -------------

# Serialize
import pickle

myFile = open("./animalsFile.dat", "wb")

animals = ["python", "monkey", "camel"]
pickle.dump(animals, myFile)

myFile.close()

# Deserialize
import pickle

myFile = open("./animalsFile.dat", "rb")

animals = pickle.load(myFile)
print(animals)

myFile.close()