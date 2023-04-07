## Strings ##

my_string = "Mi cadena."
my_other_string = "Mi otra cadena."

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Está es una cadena con\nsalto de línea."
print(my_new_line_string)

my_tab_string = "\tEstá es una cadena con tabulación."
print(my_tab_string)

my_scape_string = "\\t Esta es una cadena con \\n escapado."
print(my_scape_string)

## Formateo ##

name, last_name, age = "David", "Ramos", 25

print("Mi nombre es {} {} y mi edad es {}.".format(name, last_name, age))
print("Mi nombre es %s %s y mi edad es %s." % (name, last_name, age))
print(f"Mi nombre es {name} {last_name} y mi edad es {age}.")

## Desempaquetado de caracteres ##

language = "python."
a, b, c, d, e, f, g = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

## División ##

language_slice = language[0:3]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-1]
print(language_slice)

## Reverse ##

reversed_language = language[::-1]
print(reversed_language)

## Funciones del sistema ##

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
print("Py" == "py")
