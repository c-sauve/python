'''
Problem #11



In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

'''

grid = [
 ['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08'],
 ['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00'],
 ['81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65'],
 ['52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91'],
 ['22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80'],
 ['24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50'],
 ['32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70'],
 ['67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21'],
 ['24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72'],
 ['21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95'],
 ['78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92'],
 ['16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57'],
 ['86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58'],
 ['19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40'],
 ['04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66'],
 ['88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69'],
 ['04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36'],
 ['20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16'],
 ['20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54'],
 ['01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']
]

adjacent_length = 4
greatest_sum = 0
adjacent_values = []
# This function will return an array of numbers from a grid going diagonal to the left


def diagonal_left(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position + x
            row_position = var_row_position - x
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(int(var_grid[column_position][row_position]))
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


# This function will return an array of numbers from a grid going diagonal to the right


def diagonal_right(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position + x
            row_position = var_row_position + x
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(var_grid[column_position][row_position])
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


def up(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position - x
            row_position = var_row_position
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(var_grid[column_position][row_position])
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


def down(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position + x
            row_position = var_row_position
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(var_grid[column_position][row_position])
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


def left(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position
            row_position = var_row_position - x
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(var_grid[column_position][row_position])
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


def right(var_grid, var_column_position, var_row_position, var_length):
    adjacent_numbers = []
    for x in range(var_length):
        try:
            column_position = var_column_position
            row_position = var_row_position - x
            if column_position < 0:
                return [0, 0, 0, 0]
            elif row_position < 0:
                return [0, 0, 0, 0]
            else:
                adjacent_numbers.append(var_grid[column_position][row_position])
        except IndexError:
            return [0, 0, 0, 0]
    return adjacent_numbers


def find_product_of_adjacent(var_grid, var_length):
    grid_length = len(var_grid)
    for column in range(grid_length):
        for row in range(grid_length):
            indexes = get_arr_of_indexes(var_grid, column, row, var_length)
            sum_of_arr_values = get_arr_sum_of_values(indexes)
            for check_values in sum_of_arr_values:
                if update_greatest_sum(check_values):
                    global adjacent_values
                    adjacent_values = indexes[sum_of_arr_values.index(check_values)]


def get_arr_sum_of_values(var_array):
    sum_values = []
    for values in var_array:
        sum_values.append(sum_of_values(values))
    return sum_values


def get_arr_of_indexes(var_grid, var_column, var_row, var_length):
    index_arr = []
    g_dl = diagonal_left(var_grid, var_column, var_row, var_length)
    g_dr = diagonal_right(var_grid, var_column, var_row, var_length)
    g_left = left(var_grid, var_column, var_row, var_length)
    g_right = right(var_grid, var_column, var_row, var_length)
    g_up = left(var_grid, var_column, var_row, var_length)
    g_down = right(var_grid, var_column, var_row, var_length)
    index_arr.append(g_down)
    index_arr.append(g_up)
    index_arr.append(g_right)
    index_arr.append(g_dl)
    index_arr.append(g_dr)
    index_arr.append(g_left)
    return index_arr


def sum_of_values(var_array):
    new_value = 1
    for entry in var_array:
        new_value = new_value * int(entry)
    return new_value


def update_greatest_sum(var_value):
    global greatest_sum
    if greatest_sum < var_value:
        greatest_sum = var_value
        return True
    return False


find_product_of_adjacent(grid, adjacent_length)
print(adjacent_values)
print(greatest_sum)
