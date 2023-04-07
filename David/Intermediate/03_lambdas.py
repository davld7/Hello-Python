## Lambdas ##

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(5, 2))

multiply_two_values = lambda first_value, second_value: first_value * second_value

print(multiply_two_values(7, 1))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(1)(5, 1))
