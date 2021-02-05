#!/usr/bin/python3

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
  if i > 3:
    break
  print(str(i))
print("")

print("Using the continue statement it will skip the rest of the code in the loop and move onto the next iteration of the loop.")
print("for i in range(5):\n  if i == 3:\n   print(str(i))\n    continue")
for i in range(5):
  if i ==  3:
    continue
  print(str(i))
print("")

print("Using the pass statement is just a place holder. Its used to be used when you want to place future code. When it hits pass nothing happens. It's good if you want to have some statement but you don't want to put anything in that statement yet.")
print("for i in range(5):\n  if i > 3:\n   print(str(i))\n    pass")
for i in range(5):
  if i > 3:
    pass
  print(str(i))
print("")

# Just for some fun lets print a pyramid and an upsidown one
print("Just for some fun lets print a pyramid and an upsidown one.")
var_length = 10
var_astr = "*"
for i in range(var_length):
    for j in range(var_length - i):
        print(" ", end="") # using end="" mean it wont print a new line
    print(var_astr)
    var_astr += "**"
    
var_range -=1
space = 1
astrNum = ((var_range*2)-1)
astr = "*" * astrNum
for i in range(var_range):
    print(" " + space * " " + astr)
    astrNum -= 2
    astr = "*" * astrNum
    space += 1