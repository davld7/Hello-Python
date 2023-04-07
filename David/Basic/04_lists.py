## Lists ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 25, 17, 17]
print(my_list)
print(len(my_list))

my_other_list = [25, 1.77, "David", "Ramos"]

print(type(my_list))
print(type(my_other_list))
print(my_other_list[0])
print(my_other_list.count("David"))
print(my_list.count(17))

age, height, name, last_name = my_other_list
print(name)

name, height, age, last_name = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("Developer")
print(my_other_list)

my_other_list.insert(1, "Gris")
print(my_other_list)
my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(17)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(1)
print(my_pop_element)
print(my_list)

del my_list[0]
print(my_list)


my_list = [25, 17]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.append(21)
print(my_new_list)
my_new_list.sort()
print(my_new_list)

# Se toma los valores del 0 hasta el 2 (omitiendo el valor 2).
print(my_new_list[0:2])

my_list = "Hola Python"
print(my_list)
print(type(my_list))
