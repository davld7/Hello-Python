## Classes ##

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


my_person = Person("Roberto David", "Morales")

print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self):
        self.name = "Roberto"
        self.surname = "Morales"


print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está caminando.")


my_person = Person("David", "Ramos")

print(my_person.full_name)

my_person.walk()

my_other_person = Person("Roberto", "Morales", "Beto")

my_other_person.walk()


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública.
        self.__name = name  # Propiedad privada.

    def get_name(self):
        return self.__name
