#!/usr/bin/python3
'''
Factorial digit sum


  [Show HTML problem content]
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

number_range = 100
factorial_sum = 1
answer = 0

for numbers in range(1, number_range):
    factorial_sum *= numbers

for values in range(len(str(factorial_sum))):
    answer += int(str(factorial_sum)[values])


print(answer)
