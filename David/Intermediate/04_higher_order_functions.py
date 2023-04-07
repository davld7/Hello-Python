## Higher Order Functions ##

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, sum_function):
    return sum_function(first_value + second_value)


print(sum_two_values_and_add_value(5, 1, sum_one))

print(sum_two_values_and_add_value(1, 1, sum_five))

## Closures ##


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(2)
print(add_closure(5))

print((sum_ten(5))(2))

## Built-in Higher Order Functions ##

numbers = [1, 2, 3, 4, 5, 6, 7, 11, 17, 19]

# Map


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))

print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_number_than_ten(number):
    if number > 10:
        return True
    else:
        return False


print(list(filter(filter_number_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

reduce_list_numbers = [1, 2, 3, 4]


def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, reduce_list_numbers))
