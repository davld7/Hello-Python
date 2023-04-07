## Regular Expressions ##

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares."
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros."

match = re.match("Esta es la lección", my_string, re.I)

print(match)

start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)

# if not(match == None): #Otra forma de comprobar el None
# if match is not None:

if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("lección", my_string, re.I)

print(search)

start, end = search.span()

print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)

print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("Expresiones", "expresiones", my_string, re.I))

print(re.sub("Lección", "LECCIÓN", my_string, re.I))

print(re.sub("Expresiones Regulares", "RegEx", my_string, re.I))

print(re.sub("lección|Lección", "LECCIÓN", my_string, re.I))

print(re.sub("[l|L]ección", "LECCIÓN", my_string, re.I))

# patterns
# https://regex101.com/

pattern = r"[l|L]ección"
findall = re.findall(pattern, my_string)
print(findall)

pattern = r"[l|L]ección|Expresiones"
findall = re.findall(pattern, my_string)
print(findall)

pattern = r"[0-9]"
findall = re.findall(pattern, my_string)
search = re.search(pattern, my_string)
print(findall)
print(search)

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "david@david.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "david@david."
print(re.findall(pattern, email))
