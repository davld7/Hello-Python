## Dictionaries ##

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "David",
                 "Apellido": "Morales", "Edad": 25, 1: "Python"}

my_dict = {"Nombre": "David", "Apellido": "Morales",
           "Edad": 25, "Lenguajes": {"Python", "Swift", "Kotlin"}, 1: "1.77"}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Roberto"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Developer."
print(my_dict)
print(my_dict["Calle"])

del my_dict["Calle"]
print(my_dict)

print("Nombre" in my_dict)
print("David" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", "Apellido"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", "Apellido"))

print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Developer")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict.values()))
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
