#!/usr/bin/python3
# This is how we create a variable

# Number
var_number = 7

# Assign a binary value (using numbers)
var_binary = 0b11110000

# String
var_string = "This is some string"

# List
var_list = ["Orange", "Apple", "Banana"]

# Tuple These values can"t change. You have to create a new tuple to make changes. These are basically a constant lists. NOTE a list uses [] where a tuple uses ()
var_tuple = (123, 456, 789)

# Dictionary
var_dict = {"Name": "Billy", "Age": "25"} # note a dictionary holds object values and can be specified using {} These values are mutable

# lists can contain any type of data type
var_mixed_list = [var_number, var_string, var_list, var_tuple, var_dict,  "Anyting can go"]

# Print a binary value
print("Lets print out a binary number. This is how you do it. print(bin(<binary_value>)")
print(bin(var_binary))

# How to concatinate strings with a numbered variable
print("The number I will print out is " + str(var_number))

# if you want to print a charcter from a string you can treat the string like an array.
print("This will print out the 3rd character in the string variable we created. " + var_string[2]) # this will print out i

# if you want to print a certain amount of characters you can put a range in.
print("Lets print out a range of characters from our variable string. " + var_string[0:4]) # this should print out This  

# How to concatinate strings with with a variable
print("To concate a string together you would type in the string then use \"+\" and then the other string. Below we will output (Hello! + var_string)")
print("Hello! " + var_string)

# Lets print out what is in a list
print("Below is a list containing different datatypes.")
print(var_mixed_list)
