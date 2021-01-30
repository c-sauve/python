'''
A palindrome is a word that is the same read backwords like racecar



A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

# lets start off figuring out how to read a palindrome
value = 9009
value = 90090


def is_palindrome(value):
    convert = str(value)
    len_of_value = len(convert)
    middle_value = -1
    num_arr = [int(x) for x in str(value)]
    if len_of_value % 2 != 0:
        #store middle number
        middle_value = round(len_of_value/2)
    #print(num_arr)
    return_val = True
    for index in range(len_of_value):

        if index * 2 > len_of_value:
            continue
        reverse_value = -1 - index
        if index == middle_value:
            continue
        if num_arr[index] == num_arr[reverse_value]:
            continue
        else:
            #print(str(value) + ' is not a palindrome')
            return_val = False
    return return_val
numbers_to_make_palindrome = []
largest_palindrome = 0
for first_num in range(1000):
    for second_num in range(1000):
        #print(str(first_num)  + " second num " + str(second_num))
        check_if_palindrome = first_num * second_num
        if is_palindrome(check_if_palindrome):
            if largest_palindrome < check_if_palindrome:
                largest_palindrome = check_if_palindrome
                numbers_to_make_palindrome = [first_num, second_num]
print(largest_palindrome)
print(numbers_to_make_palindrome)