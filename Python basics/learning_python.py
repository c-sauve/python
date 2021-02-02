#!/bin/python

# The above is how you tell the interpreter which python interpreter to use. Similar to bash scripts at the top you would use #!/bin/bash

'''
This is how 
to create a
multi line comment
'''

# How to print out to the console you use the print() function
print("Hello world")

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

# Now lets get into operators

#Addition (+)
print("1 + 2 = " + str(1 + 2))

#Subtraction (-)
print("10 - 5 = " + str(10 - 5))

#Multiplication (*)
print("10 * 12 = " + str(10 * 12))

#Modulus (%) (The remander after a division) I.e 5 % 2 = 1
print("5 % 2 = " + str(5 % 2))

#Exponent (**)
print("5**2 = " + str(5 ** 2))

#Divistion (/) (Normal divison which can spit out an int, float, or long) i.e 5 / 2 = 2.5
print("5 / 2 = " + str(5 / 2))

#Floor Divis
print("5 // 2 = " + str(5 // 2))

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

# Assigning Values and Bitwise Operations

# lets start with a number variable of 10
var_new_number = 10
print("Creating a new number variable to be used and reassigned. The starting number is " + str(var_new_number))

# now lets re assign that value in different ways using our operators.
  # One way is to re use the variable like this 
var_new_number = var_new_number + 10
print("Re-assigning the last variable using the method variable = variable + 10 which now is -> " + str(var_new_number))

# A more practicle approach is to use the operatore=. I.e
var_new_number += 10
print("Re-assigning the last variable using the method variable += 10 which now is -> " + str(var_new_number))
var_new_number -= 10                                             
print("Re-assigning the last variable using the method variable -= 10 which now is -> " + str(var_new_number))
var_new_number *= 10                                             
print("Re-assigning the last variable using the method variable *= 10 which now is -> " + str(var_new_number))
var_new_number **= 10                                            
print("Re-assigning the last variable using the method variable **= 10 which now is -> " + str(var_new_number))
var_new_number /= 10                                             
print("Re-assigning the last variable using the method variable /= 10 which now is -> " + str(var_new_number))
var_new_number //= 10                                            
print("Re-assigning the last variable using the method variable //= 10 which now is -> " + str(var_new_number))

# Binary operations
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


# Logical Operators (and, or, not)
print("Logical Operator (and, or, not)")
print("The or operator will evaluate True if one of the values are True")
print("((4 > 5) or (3 < 4)) = " + str((4 > 5) or (3 < 4)))
print("The and operator this will evaluate True if both of the values are True")
print("((4 > 5) and (3 < 4)) = " + str((4 > 5) and (3 < 4)) )
print("The is operator this will evaluate True if both values are the same")
print("((4 > 5) is (3 < 4)) = " + str((4 > 5) is (3 < 4)) )
print("The is no operator this will evaluate True if both values are not the same")
print("((4 > 5) is not (3 < 4)) = " + str((4 > 5) is not (3 < 4)) )
# Identity Operators
print("Identity Operator")
# Membership Operators (Is something contained in something else) these aren't used often
print("Membership Operators (Is something contained in something else)")
var_new_list = [1, 2, 3, 4]
print("Here we have a list of value. " + str(var_new_list))
print("Lets check if a value is in the list. If it is it will return true")
print("25 in [1, 2, 3, 4] = " + str(25 in var_new_list))
print("Lets check if a value is not in the list. If it is it will return true")
print("25 not in [1, 2, 3, 4] = " + str(25 not in var_new_list))
# Operator Precedence
print("operator Precedence")
print("This is just a list of operators that take precedence over the other. Here is a list of least precedence to most precedence.")
print(":=, lambda, if - else, or, and, not x, (in, not in, is, is not, <, <=, >=, !=, ==), ( |, ^), &, ( <<, >> ), ( +, - ), ( *, @, /, //, % ), \n( +x, -x, ~x), **, await x, ( x[index], x[index:index], x(arguments...), x.attribute), (expressions...), [expressions...], {key: value..}, {expressions..}") 

# Loops and conditional statements
print("There are different types of loops out there. i.e While, for, and conditionals / nested loops")

# While loop
print("Lets start with a while loop. This type of loop keeps going until you break it or when it evaluates to true.")
print("var_x = 0\nwhile var_x < 3: \n  print(str(var_x)) \n  var_x +=1\n")
var_counter = 0
while var_counter < 3:
  print("output of while loop is " + str(var_counter))
  var_counter +=1

print("")

# For loop
print("There are many different types of for loops out there. In this case we will do a range of 5. It starts at 0 up to 4 this counts as a range of 5 since it starts at 0")
print("for i in range(0, 5):\n  print(\"*\" i)\n")
for i in range(0, 5):
  print("*" * i) # this will multiply the character * by i

print("")

# Nested Loops
print("Nested loops are just a mixture of for and or while loops within themselves.")
print("For this example we will use nested for loop because they are the more common ones.")
print("In this nested loop we will have loops using a range of numbers then we will add those numbers together.")
print("for i in range(0, 2):\n  for k in range(3): \n    print(str(i + j))\n")
for i in range(0, 2):
  for j in range(3):
    print(str(i) + " + " + str(j) + " = " + str(i + j))

print("")


# Conditional Statements (continue, break, pass)
print("Using the break statement it will break out of the loop. In this example we will stop the loop once it reaches 3")
print("for i in range(10):\n  if i > 5:\n   print(str(i))\n    break")
for i in range(10):
  if i > 5:
    break
  print(str(i))
print("")

print("Using the continue statement it will skip the rest of the code in the loop and move onto the next iteration of the loop.")
print("Using the pass statement is just a place holder. Its used to be used when you want to place future code. When it hits pass nothing happens. It's good if you want to have some statement but you don't want to put anything in that statement yet.")


# Just for some fun lets print a pyramid 
var_length = 10
var_astr = "*"
for i in range(var_length):
    for j in range(var_length - i):
        print(" ", end="") # using end="" mean it wont print a new line
    print(var_astr)
    var_astr += "**"
    