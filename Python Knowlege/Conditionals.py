#!/usr/bin/python3

# In this file we will describe some of the different conditionals.
print("Like all coding languages there are the standard if, else if, else conditional statements.\nThose statements look like this.")
print("var_value = 4\nif var_value > 10:\n  print(str(var_value) + \" is larger than 10\") \nelif var_value == 10:\n  print(str(var_value) + \" is equal to 10\") \
\nelse: \n  print(str(var_value) + \" is less than 10)\n")
var_value = 4
if var_value > 10:
    print(str(var_value) + " is larger than 10")
if var_value == 10:
    print(str(var_value) + " is equal to 10")
else:
    print(str(var_value) + " is less than 10")
    
print("\n")
print("There can even be more than one <statement> on the same line, separated by semicolons:")

print("if <expr>: <statement_1>; <statement_2>; ...; <statement_n>")

print("But what does this mean? There are two possible interpretations:")

print("    If <expr> is true, execute <statement_1>.")

print("    Then, execute <statement_2> ... <statement_n> unconditionally, irrespective of whether <expr> is true or not.")

print("    If <expr> is true, execute all of <statement_1> ... <statement_n>. Otherwise, don\'t execute any of them.")

print("if \"f\" in \"foo\": print(\"We\"); print(\"have\"); print(\"Foo\")")
if "f" in "foo": print("We"); print("have"); print("Foo")

print("\n")
'''

Conditional Expressions (Python's Ternary Operator)

This is different from the if statement forms listed above because it is not a control structure that directs the flow of program execution. 
It acts more like an operator that defines an expression. In the above example, <conditional_expr> is evaluated first. 
If it is true, the expression evaluates to <expr1>. If it is false, the expression evaluates to <expr2>.

Notice the non-obvious order: the middle expression is evaluated first, and based on that result, one of the expressions on the ends is returned. 
Here are some examples that will hopefully help clarify:

'''
print("This is a ternary operator conditional")
print("print(\"One is \", \"greater than two\" if 1 > 2 else \"less than two\"")
print("one is", "greater than two" if 1 > 2 else "less than two")