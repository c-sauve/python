'''
Task:
Find all the natural numbers within a ragne of numbers.
Then find the sum of all those natural numbers.

The natural numbers we want to find are 3 and 5. The range will be 1000.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

# Functions

'''
The purpose of this function is to find all the natural numbers within a range.
param one -> natural_number is the number we will increment by to find what numbers of that increment fit within the range
param two -> number_range the range in which you want to find all the natural numbers of a given number
return array_of_numbers -> this will be an array of all the natural numbers within the range.

'''
def find_sum_of_natural_numbers(natural_number, number_range):
    array_of_numbers = []
    #for i = number_range; i > 0; i - natural_number:
    for numbers in range(natural_number, number_range, natural_number):
        array_of_numbers.append(numbers)
    return array_of_numbers


# This was a different way to go about solving this problem that I found online. (WOW its not complicated like mine haha)
# The purpose of this function is to return the sum of all the the multiples of 3 and 5 within a range of 1000.
def other_method():
    counter = 0
    for i in range (1000):
        if (i%3 == 0) | (i%5 == 0):
            counter = counter + i
    print(counter)


'''
The purpose of this function is to return the sum of all the the multiples of 3 and 5 within a range of 1000.
return sum_of_all -> this will return a number.
'''
def multiples_of_three_and_five():
    # lets find all the multiples of 3 within the range of 1000
    array_of_three = find_sum_of_natural_numbers(3, 1000)
    # lets find all the multiples of 5 within the range of 1000
    array_of_five = find_sum_of_natural_numbers(5, 1000)
    # lets print out all the multiples of 3 and 5 withing the range of 1000
    print(array_of_three)
    print(array_of_five)
    # now we must remove the numbers that duplicate within both arrays
    for multiples_of_three in array_of_three:
        if multiples_of_three in array_of_five:
            array_of_five.remove(multiples_of_three)
    sum_of_three = sum(array_of_three)
    sum_of_five = sum(array_of_five)
    sum_of_all = sum_of_three + sum_of_five
    return sum_of_all


sum_of_multiples = multiples_of_three_and_five()
print(sum_of_multiples)
other_method()