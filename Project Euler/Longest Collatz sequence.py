#!/usr/bin/python3

'''
Problem 14



The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''


def even_value(var_value):
    return var_value/2


def odd_value(var_value):
    #print(var_value)
    if var_value == 1:
        return var_value
    return var_value * 3 + 1


def get_new_number(var_value):
    if var_value % 2 == 0:
        return even_value(var_value)
    else:
        return odd_value(var_value)


def find_chain(var_number, var_chain_arr):
    list_of_values = []
    number = var_number
    #print(number)
    while number != 1:
        list_of_values.append(int(number))
        number = get_new_number(int(number))
    list_of_values.append(int(number))
    return list_of_values


chain_number_range = 1000000

chain = [0]
found_number = 0
for i in range(1, chain_number_range):
    # I'm skipping the even numbers because if its odd there there is a guarantee to be an even number.
    # While even numbers / 2 can still be another even number.
    if i % 2 == 0:
        continue
    if i in chain:
        continue
    print(i)
    new_chain = find_chain(i, chain)
    if len(new_chain) > len(chain):
        chain = new_chain
        found_number = i

print(len(chain))
print(found_number)

