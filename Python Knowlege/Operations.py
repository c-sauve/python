#!/usr/bin/python3

# operators return a boolean. They are commonly used in if, while, and for statements
#Equal to (==)
print("5 == 5 will result in " + str(5 == 5))  # This will return True
print("5 == 6 will result in " + str(5 == 6)) # This will return False

#Not equal to (!=) or (<>) (<> is no longer in use after python 3 or above but it can be used in python 2 or below)
print("5 != 3 will result in " + str(5 != 3)) # This will return True
print("5 != 5 will result in " + str(5 != 5)) # This will return False

#Greater than (>)
print("5 > 3  will result in " + str(5 > 3))# This will return True

#Greater than or equal to (>=)
print("5 >= 3 will result in " + str(5 >= 3)) # This will return True

#Less than (<)
print("5 < 3 will result in " + str(5 < 3))# This will return False

#Less than or equal to (<=)
print("5 <= 3 will result in " + str(5 <= 3)) # This will return False

# Binary operations
# Assigning Values and Bitwise Operations
print("Lets play with binary operations")
var_binary_a = 0b11001100
var_binary_b = 0b11110000
print("The two binary values we will be using are " + bin(var_binary_a) + " and " + bin(var_binary_b)) 
print("The numbers both those binary values produce are " + str(var_binary_a) + " and " + str(var_binary_b)) 
print("Operations with Binary go as following. \n Using & (and) means if both sides have a 1 it will stay. Otherwise if a 0 value is involved it will produce a 0 even if the other value has a 1.")
print("For example bin(" + bin(var_binary_a) + " & " + bin(var_binary_b) + ") will result in " + bin(var_binary_a&var_binary_b)) 
print("Using | (or) means any values with a 1 will stay even if the other value has a 0. If both values have a 0 then it will be 0")
print("For example bin(" + bin(var_binary_a) + " | " + bin(var_binary_b) + ") will result in " + bin(var_binary_a|var_binary_b)) 
print("Using >> (a right shift) this means we will move the values to the right x amount of places. In this example lets use 3. So we will shift all the values three slots to the right.")
print("For example bin(" + bin(var_binary_a) + " >> 3 ) will result in " + bin(var_binary_a >> 3) + " the value now is " + str((var_binary_a << 3)))
print("Using << (a left shift) this means we will move the values to the right x amount of places. In this example lets use 3. So we will shift all the values three slots to the right.")
print("For example bin(" + bin(var_binary_a) + " << 2 ) will result in " + bin(var_binary_a << 2) + " the value now is " + str((var_binary_a << 2)))
