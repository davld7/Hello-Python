## Exception Handling ##

number_one = 5
number_two = 2
number_two = "2"

try:
    print(number_one+number_two)
    print("No se ha producido un error.")
except:
    # Se ejecuta si se produce una excepción.
    print("Se ha producido un error.")

try:
    print(number_one+number_two)
    print("No se ha producido un error.")
except:
    print("Se ha producido un error.")
else:  # Opcional.
    # Se ejecuta si no se produce una excepción.
    print("La ejecución continúa correctamente.")
finally:  # Opcional.
    # Se ejecuta siempre.
    print("La ejecución continúa.")

# Excepciones por tipo.

try:
    print(number_one+number_two)
    print("No se ha producido un error.")
except ValueError:
    print("Se ha producido un ValueError.")
except TypeError:
    print("Se ha producido un TypeError.")

# Captura de la información de la excepción.

try:
    print(number_one+number_two)
    print("No se ha producido un error.")
except ValueError as error:
    print(error)
# except TypeError as error:
#     print(error)
except Exception as exception:
    print(exception)
