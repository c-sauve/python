#!/usr/bin/python3

'''
Problem 15


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
D = Down
R = Right
example is 2R2mD, 1R1D1R1D, 1R2D1R 1D2R1D 1D1R1D1R 2D2R

How many such routes are there through a 20×20 grid?
---
 We need to to use choose (some math term) to figure out the answer
 The formula for choose is nCk = n! / k! ( n - k )
! = factorial
n = objects
C = choose
k =  select

example n = 4 k = 2 
this is for a 2x2 grid
4! / 2! ( 4 - 2)
(4*3*2*1) / (1 * 2) ( 1 * 2)
24 / 4 = 6
'''

import math

grid_x = 20
grid_y = 20
grid_size = grid_x + grid_y


# This all works when we are under the assumption that we are starting at one corner of the grid and trying to get to
# the opposite end of the grid.


def choose(n, k):
    object_factorial = factorials(n)
    select_factorials = factorials(k)
    nk = factorials(n - k)
    options = object_factorial / (select_factorials * nk)
    return int(options)


def factorials(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


print(choose(grid_size, grid_y))

# math also has a choose function that we can use
# print(math.comb(grid_size, grid_y))
