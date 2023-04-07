## Tuples ##
# A diferencia de las listas las tuplas son inmutables.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.77, "David", "Ramos")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("David"))
print(my_tuple.index("David"))

my_other_tuple = (17, 11)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_tuple[0:3])

my_tuple = list(my_tuple)  # Convertir a List.
print(type(my_tuple))
print(my_tuple)
my_tuple[3] = "Morales"
print(my_tuple)
