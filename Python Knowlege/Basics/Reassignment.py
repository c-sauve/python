#!/usr/bin/python3

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

# Re-assigning values in a list
var_list = ["Apple", "Orange", "Banana"]
print("This is our list " + str(var_list))
# Re-assigning orange to grape
var_list[1] = "Grape"
print("Re-assigning the the Orange Value to be Grape. var_list[1] = Grape -> " + str(var_list))

# Re-assigning values in a list
var_dictionary = {"Name": "Bob", "Age": 25}
print("This is our dictionary " + str(var_dictionary))
# Re-assigning orange to grape
var_dictionary["Age"] = "30"
print("Re-assigning the the Age Value to be 30. var_dictionary[\"Age\"] = 30 -> " + str(var_dictionary))
    