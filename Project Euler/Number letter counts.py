#!/usr/bin/python3

'''
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage

'''
zero = 'Zero'
one_digit = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
two_digits = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
three_digits = 'Hundred'
four_digits = 'Thousand'

doubles = 'ty'
triples = 'Hundred'
quadruples = 'Thousand'


def num_to_string(var_number):
    return str(var_number)


def get_word_length(var_word):
    return len(var_word)


def double_digits(var_num):
    word = ''
    string_number = num_to_string(var_num)
    word_length = get_word_length(string_number)
    if word_length == 2:
        if int(string_number[0]) == 1:
            if int(string_number[1]) == 0:
                word = two_digits[0]
            else:
                word = teens[int(string_number[1]) - 1]
        else:
            if int(string_number[1]) == 0:
                word = two_digits[int(string_number[0]) - 1]
            else:
                word = two_digits[int(string_number[0]) - 1] + "-" + single_digits(int(string_number[1]))
    return word


def single_digits(var_num):
    word = ''
    string_number = num_to_string(var_num)
    word_length = get_word_length(string_number)
    if word_length == 1:
        if int(var_num) == 0:
            word = zero
        else:
            word = one_digit[int(var_num) - 1]
    return word


def triple_digits(var_num):
    string_number = num_to_string(var_num)
    hundreds = single_digits(int(string_number[0])) + " " + three_digits
    if int(string_number[1]) == 0 and int(string_number[2]) == 0:
        rest_of_word = ''
    elif int(string_number[1]) == 0:
        rest_of_word = " and " + single_digits(int(string_number[2]))
    else:
        rest_of_word = " and " + double_digits(int(string_number[1] + string_number[2]))
    return hundreds + rest_of_word


def quadruple_digits(var_num):
    string_number = num_to_string(var_num)
    thousands = single_digits(int(string_number[0])) + " " + quadruples
    if int(string_number[1]) == 0 and int(string_number[2]) == 0 and int(string_number[3]) == 0:
        rest_of_word = ''
    elif int(string_number[1]) == 0 and int(string_number[2]) == 0 and int(string_number[3]) > 0:
        rest_of_word = " and " + single_digits(int(string_number[3]))
    elif int(string_number[1]) == 0 and int(string_number[2]) > 0:
        rest_of_word = " and " + double_digits(int(string_number[2] + string_number[3]))
    else:
        rest_of_word = " " + triple_digits(int(string_number[1] + string_number[2] + string_number[3]))
    return thousands + rest_of_word


#print(double_digits(39))
#print(single_digits(4))
#print(triple_digits(629))
#print(quadruple_digits(1199))


def word_length(var_word):
    new_list = list(var_word)
    if '-' in new_list:
        new_list.remove('-')
    if ' ' in new_list:
        for i in range(new_list.count(' ')):
            new_list.remove(' ')
    #print(new_list)
    return len(new_list)


#test = double_digits(90)
#print(word_length(test))


def count_range_of_letter(var_range):
    list_of_number_length = []
    for numbers in range(1, var_range + 1):
        word = ''
        if numbers < 10:
            word = single_digits(numbers)
        elif numbers < 100:
            word = double_digits(numbers)
        elif numbers < 1000:
            word = triple_digits(numbers)
        elif numbers < 10000:
            word = quadruple_digits(numbers)
        else:
            print("We haven't accounted for numbers that large sorry. WIP ;P")
        list_of_number_length.append(word_length(word))
    return sum(list_of_number_length)


number_range = 1000
print(count_range_of_letter(number_range))
