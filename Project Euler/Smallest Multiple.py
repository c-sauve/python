'''
Problem #5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
cont = True
counter = 1
var_range = 20
while cont:
    counter += 1

    for y in range(1, var_range+1):
        if counter % y != 0:
            break
        if y == var_range:
            cont = False
            print(counter)
    #cont = False
    #print(counter)
