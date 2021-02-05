#!/usr/bin/python3

# Now lets get into operators

# Addition (+)
print("Addition: 1 + 2 = " + str(1 + 2))

# Subtraction (-)
print("Subtraction 10 - 5 = " + str(10 - 5))

# Multiplication (*)
print("Multiplication: 10 * 12 = " + str(10 * 12))

# Modulus (%) (The remander after a division) I.e 5 % 2 = 1
print("Modulus: 5 % 2 = " + str(5 % 2))

# Exponent (**)
print("Exponent: 5**2 = " + str(5 ** 2))

# Divistion (/) (Normal divison which can spit out an int, float, or long) i.e 5 / 2 = 2.5
print("Division: 5 / 2 = " + str(5 / 2))

# Floor Divis
print("Floor division: 5 // 2 = " + str(5 // 2))

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