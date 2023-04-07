## Error Types ##

# SyntaxError

# print "Hola python!" #Descomentar
print("Hola python!")

# NameError

language = "Spanish" #Comentar
print(language)

# IndexError

my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]

# print(my_list[5]) #Descomentar

# ModuleNotFoundError

# import maths #Descomentar

import math

# AttributeError

# print(math.PI) #Descomentar
print(math.pi)

# KeyError

my_dict = {"Name": "David", "Apellido": "Ramos"}

# print(my_dict["Nam"]) # Descomentar

# TypeError

# print(my_list["a"]) #Descomentar

print(my_list[0])
print(my_list[True])
print(my_list[False])

# ImportError

# from math import PI # Descomentar

from math import pi
print(pi)

# ValueError

my_int = int("10")
# my_int = int("10 Años") #Descomentar
print(my_int)

# ZeroDivisionError

print(4/2)
# print(4/0) Descomentar
