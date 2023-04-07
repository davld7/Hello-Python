## File Handling ##

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe.
txt_file = open("David/Intermediate/my_file.txt", "w+")
txt_file.write(
    "My name is David\nMy lastname is Ramos\n25 years old\nMy favorite languages is Python")

# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readlines())

# for line in txt_file.readlines():
#     print(line)

txt_file.close()

with open("David/Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nand C#")
    my_other_file.close()

with open("David/Intermediate/my_file.txt", "r+") as my_read_file:
    for line in my_read_file:
        print(line)

# os.remove("David/Intermediate/my_file.txt")

# .json file


json_file = open("David/Intermediate/my_file.json", "w+")

json_test = {"name": "David", "surname": "Ramos", "age": 25,
             "language": ["Python", "Kotlin", "Swift", "C#"], "website": "https://github.com/davld7"}

json.dump(json_test, json_file, indent=2)


json_file.close()

with open("David/Intermediate/my_file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)

json_dict = json.load(open("David/Intermediate/my_file.json"))

print(json_dict)

print(type(json_dict))

print(json_dict["name"])

# .csv file


csv_file = open("David/Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["David", "Ramos", 25, "Python",
                    "https://github.com/davld7"])

csv_file.close()

with open("David/Intermediate/my_file.csv") as my_file_csv:
    for line in my_file_csv:
        print(line)

# .xlsx file

# import xlrd # Debe instalarse el módulo

# .xml file
