#!/usr/bin/python3
'''
Amicable numbers


Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

check_amicable_num = 10000


def get_divisors(var_num):
    var_array = []
    if (var_num == 0) or (var_num == 1):
        return []
    for var_numbers in range(1, var_num):
        if int(round(var_num / 2)) < var_numbers:
            break
        if (var_num % var_numbers) == 0:
            var_array.append(var_numbers)
    return var_array


def find_amicable_pair(var_one):
    d_of_a_divisors = get_divisors(var_one)
    # print(d_of_a_divisors)
    sum_of_d_of_a = sum(d_of_a_divisors)
    # print(sum_of_d_of_a)
    d_of_b_divisors = get_divisors(sum_of_d_of_a)
    # print(d_of_b_divisors)
    sum_of_d_of_b = sum(d_of_b_divisors)
    if sum_of_d_of_b != sum_of_d_of_a:
        if sum_of_d_of_b == var_one:
            return sum_of_d_of_a
    return 0


# Find all the amicable pairs that are under 10000 and find the sum of that.
new_amicable_pairs = []

counter = 2
while counter <= check_amicable_num:
    check_value = find_amicable_pair(counter)
    if check_value != 0:
        if check_value < check_amicable_num:
            if check_value not in new_amicable_pairs:
                new_amicable_pairs.append(check_value)
            if counter not in new_amicable_pairs:
                new_amicable_pairs.append(counter)
    counter += 1

print(new_amicable_pairs)
print(sum(new_amicable_pairs))

