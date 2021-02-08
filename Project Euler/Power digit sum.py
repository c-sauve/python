#!/usr/bin/python3

'''
Problem 16



2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''


def exponent(number, power):
    return number ** power


def sum_numbers(number):
    string_num = str(number)
    num_arr = []
    for i in range(len(string_num)):
        num_arr.append(int(str(string_num[i])))
    return sum(num_arr)


base_number = 2
base_exponent = 1000

power_num = exponent(base_number, base_exponent)
print(sum_numbers(power_num))
