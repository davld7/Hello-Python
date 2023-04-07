## Functions ##

def my_function():
    print("Esto es una función.")


my_function()


def sum_two_values(first_value, second_value):
    print(first_value + second_value)


sum_two_values(4, 3)
sum_two_values("4", "3")
sum_two_values(7.0, 0.7)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


print(sum_two_values_with_return(4, 3))

my_variable = sum_two_values_with_return(4, 3)

print(my_variable)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("David", "Ramos")

print_name(surname="Ramos", name="David")


def print_name_with_default(name, surname, profession="No profession"):
    print(f"{name} {surname} {profession}")


print_name_with_default("David", "Ramos")
print_name_with_default("David", "Ramos", "Developer")


def print_texts(*text):
    print(text)


print_texts("Roberto", "David", "Morales", "Ramos")


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("David", "Morales", "Ramos")
