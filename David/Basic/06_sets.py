## Sets ##

my_set = set()
my_other_set = {}  # Inicialmente un diccionario.

print(type(my_set))
print(type(my_other_set))

my_other_set = {25, "David", "Ramos"}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Roberto")
print(my_other_set)  # Un Set no es una estructura ordenada.

my_other_set.add("Roberto")
print(my_other_set)  # Un Set no admite repetidos.

# Sintaxis para comprobar si existe un valor en un Set.
print("David" in my_other_set)
print("Linda" in my_other_set)

my_other_set.remove("Roberto")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
# print(my_other_set) Error, el objeto no está definido.

my_set = {25, "David", "Ramos"}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"python", "javascript", "c#"}

my_new_set = my_set.union(my_other_set).union({"java", "c++"})
print(my_new_set)

print(my_new_set.difference(my_set))
