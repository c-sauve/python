'''
Problem #6

The sum of the squares of the first ten natural numbers is,

        1^2 + 2^2 ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
        ( 1 + 2  ... 10)^2 == 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
square_numbers = []
natural_numbers = []
var_rang_of_numbers = 100
for numbers in range(1, var_rang_of_numbers+1):
    natural_numbers.append(numbers)
    square_numbers.append((numbers * numbers))

sum_natural_numbers = (sum(natural_numbers) * sum(natural_numbers))
sum_of_square_numbers = sum(square_numbers)
sum_diff = sum_natural_numbers - sum_of_square_numbers
print(sum_diff)



