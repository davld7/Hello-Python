## Python Package Manager ##

# pip install pip

# pip https://pypi.org

from mypackage import arithmetics
import requests  # pip install requests
import pandas  # pip install pandas
import numpy  # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([1, 2, 3, 4, 5, 6, 7])

print(type(numpy_array))

print(numpy_array * 2)

# pip list
# pip uninstall pandas
# pip show numpy

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetics.sum_two_values(5, 2))
