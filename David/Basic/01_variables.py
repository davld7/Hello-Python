## Variables ##

my_str_variable = "My string variable"
print(my_str_variable)

my_int_variable = 7
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print.
print(my_str_variable, my_int_variable, my_bool_variable)
print("Esto es el valor de la variable:", my_bool_variable)

# Conversión de int a str.
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Algunas funciones del sistema.
print(len(my_str_variable))

# Variables en una sola línea. ¡Cuídado de abusar de esta sintaxis!
name, surname, age = "David", "Ramos", 25
print("Me llamo:", name, surname, ". Mi edad es:", age)

# Lectura de datos en terminal.

first_name = input("¿Cuál es tu nombre?: ")
last_name = input("¿Cuál es tu apellido?: ")
print("Mi nombre es:", first_name)
print("Mi apellido es:", last_name)

# Cambiamos su tipo.

name = 25
age = "David"
print(name)
print(age)

# ¿Forzamos el tipo?.

address: str = "Mi dirección"
address = 7
print(address)
