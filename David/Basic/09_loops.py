## Loops ##

## While ##

my_conditional = 0

while my_conditional < 10:
    print(my_conditional)
    my_conditional += 1
else:  # Es opcional.
    print("Mi condición no se cumple.")

while my_conditional <= 20:
    print(my_conditional)
    my_conditional += 1
    if my_conditional == 15:
        print("Se detiene el bucle.")
        break
else:
    print("No se cumple mi condición.")

## For ##

my_list = [10, 11, 17]

for element in my_list:
    print(element)

my_dict = {"Nombre": "David", "Apellido": "Morales", "Profesión": "Developer"}

for element in my_dict:  # Se almacena las keys y no los values.
    print(element)

for element in my_dict.values():  # Se almacena los values y no las keys.
    print(element)
    if element == "Morales":
        print("Hay un valor que coincide con la condición dada.")
        break  # El ciclo se detiene.
else:
    print("El bucle for se ha finalizado.")

for element in my_dict.values():  # Se almacena los values y no las keys.
    print(element)
    if element == "David":
        print("Hay un valor que coincide con la condición dada.")
        # El ciclo continúa pero partiendo de nuevo del for y no imprime "Se ejecuta.".
        continue
    print("Se ejecuta.")
else:
    print("El bucle for se ha finalizado.")
