#!/usr/bin/python3

# Lets create some test functions on how to add,subtract, multiply, and divide
def add(num_one, num_two):
    return num_one + num_two

def subtract(num_one, num_two):
    return num_one - num_two

def multiply(num_one, num_two):
    return num_one * num_two

def divide(num_one, num_two):
    if num_one == 0 or num_two == 0:
        print("We can't divide by 0 please use a different number")
        return

    return num_one / num_two


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(0, 5))
print(divide(10, 0))