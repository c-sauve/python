#!/usr/bin/python3

'''

Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''

# Lets create a list of those numbers
triangle_list = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

#triangle_list = [
#    [3],
#    [7, 4],
#    [2, 4, 6],
#    [8, 5, 9, 3],
#]


def add_numbers_from_array(var_array, var_number):
    return sum(var_array) + var_number


# This will find all the largest numbers going top down. It doesn't solve the problem.
# I'm keeping it here so I can use it for future work if needed.
index = 0
list_of_values = []
for i in range(len(triangle_list)):
    if len(triangle_list[i]) == 0:
        continue
    elif len(triangle_list[i]) == 1:
        list_of_values.append(triangle_list[i][0])
    else:
        #print(index)
        adjacent_right = index + 1
        adjacent_left = index
        if adjacent_right > len(triangle_list[i]):
            adjacent_right = index
            adjacent_left = index - 1
        if adjacent_left < 0:
            adjacent_left = index
        check_left = add_numbers_from_array(list_of_values, triangle_list[i][adjacent_left])
        check_right = add_numbers_from_array(list_of_values, triangle_list[i][adjacent_right])
        #print(triangle_list[i][adjacent_left], triangle_list[i][adjacent_right])
        if check_right > check_left:
            list_of_values.append(triangle_list[i][adjacent_right])
            index = adjacent_right
        else:
            list_of_values.append(triangle_list[i][adjacent_left])
            index = adjacent_left


# So it seems its best to work from the bottom up of the triangle than going top down.
new_list = []
for i in reversed((range(len(triangle_list)))):
    check_numbers = []
    print(new_list)
    if len(new_list) < 1:
        new_list = triangle_list[i]
        continue
    for j in range(len(triangle_list[i])):
        if (triangle_list[i][j] + new_list[j]) > (triangle_list[i][j] + new_list[j + 1]):
            check_numbers.append(triangle_list[i][j] + new_list[j])
        else:
            check_numbers.append(triangle_list[i][j] + new_list[j + 1])
    new_list = check_numbers

print(new_list)







