#!/urs/bin/pyton3

# This file is all about using the math library
import math

print("Lets go through a couple of the functions provied by math.")
print("For more information on the math library see https://docs.python.org/3/library/math.html")
# pi function
print("Who likes pie? I like Pie so lets see what Pie we have!\nprint(math.pi)")
print(math.pi)

print("Exponential function.")
print("math.e")
print(math.e)

print("Are you tired of find 2xPi well worry no more we can use the math.tau.")
print("math.tau)")
print(math.tau)

print("Do we want to find the remainder without having to use the %. Well we can using math! This function returns a float value.")
print("if we want to find the mod value of something use % if you want an int, use fmod for a float value.")
print("mod is based off of a C library.")
print("math.fmod(10, 4)")
print(math.fmod(10, 4))

print("To find a nmber raised by the power of y there are many ways to find it.")
print("1) You can use x ** y operand. This wil return an int/float value.")
print("2) You can use the pow(x, y) function. This will return an int values. It doesn't work well if you want to use float values")
print("3) You can use math.pow(x, y). This will return a float values. This function won't work if you use a negative value to the power of a float")
print("math.pow(2,2)")
print(math.pow(2,2))

print("The ceil function takes any fraction and raises it to the next int")
print(math.ceil(math.pi))
print("math.ceil(math.pi)")
print("The floor function takes away the fraction and leaves it as an int")
print("math.floor(math.pi)")
print(math.floor(math.pi))

print("Lets find the sum of some values and return a float and helps round values.")
sum_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print("sum_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]")
print("math.fsum(sum_list)")
print(math.fsum(sum_list))

print("This is the sum function in python.")
print("sum(sum_list)")
print(sum(sum_list))
