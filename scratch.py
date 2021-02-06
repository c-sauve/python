'''
This is just a scratch page to test out random code.

'''
import sympy
# lets see if we can find the lowest prime factors for a number.

def find_smallest_primes(value):
    smallest_primes = []
    while not sympy.isprime(int(value)):
        if int(value) == 1:
            break
        for prime_numbers in sympy.primerange(1, value):
            if int(prime_numbers) == 1:
                break
            if value % prime_numbers == 0:
                if int(value) != 1 or int(prime_numbers) != 1:
                    smallest_primes.append(prime_numbers)
                value /= prime_numbers
                print(int(value))
                print(prime_numbers)

    if int(value) != 1:
        smallest_primes.append(int(value))

    return sorted(smallest_primes, reverse=True)


def get_prime_numbers(var_range):
    prime_numbers = []
    for numbers in range(1, var_range):
        prime_numbers.append(sympy.prime(numbers))
    return prime_numbers


def find_powers_of_primes(var_array):
    list_of_powers = []
    prime_number_decomposition = 1
    for values in var_array:
        check_value = values - 1
        if check_value > 0 and not sympy.isprime(check_value):
            list_of_powers.append(check_value)
    # We need to add the +1 so we can get the prime number from the specified value. That is because it when it looks it
    #   starts at the value 0. So if we put in a value of 5 it goes 0,1,2,3,4 but we will need that value 5 hence the +1
    list_prime_numbers = get_prime_numbers(len(list_of_powers) + 1)

    for index in range(len(list_of_powers)):
        #print(list_of_powers[index], list_prime_numbers[index])
        prime_number_decomposition *= list_prime_numbers[index] ** list_of_powers[index]
    return prime_number_decomposition

'''
I used this link to help me understand how to find the right number
https://math.stackexchange.com/questions/2487305/how-is-the-prime-number-decomposition-theorem-correctly-used
'''
value = 15
small_primes = find_smallest_primes(value)
print(small_primes)
print(find_powers_of_primes(small_primes))


def is_triangle_number(value):
    check = value*(value+1)/2
    return check


result = is_triangle_number(4)
print(result)


def reverse_triangle(value):
    prime = get_largest_prime(value)
    check = value/(prime - 1)*2
    # My guess to get the right value is to create an array of the divisors for the triangle

    # then take (array[-2] + 1) / (array[1] +1) if array[-2] % 2 != 0
    return check


def get_largest_prime(value):
    for numbers in sorted(sympy.primerange(1, value), reverse=True):
        if value % numbers == 0:
            return numbers

    return 1


print(reverse_triangle(result))

'''
N = p1^a1 * p2^a2 * p3^a3 ... ect
pn 
where pn is a distinct prime number, and an is its exponent.
For example, 28 = 2^2 * 7^1
Furthermore, the number of divisors D(N) of any integer N can be computed from:
D(N) = (a1 + 1) * a2 + 1) * (a3 + 1) * ...
an being the exponents of the distinct prime numbers which are factors of N
For example, the number of divisors of 28 would thus be: 
D(28) = (2+1)((1+1) = 3(2 = 6 
'''


def find_divisors(var_array_of_small_primes):
    duplicates = {}
    num_of_divisors = 1
    for values in var_array_of_small_primes:
        if values in duplicates:
            continue
        else:
            duplicates[values] = var_array_of_small_primes.count(values)
    for divisors in duplicates:
        num_of_divisors *= (duplicates[divisors] + 1)

    return num_of_divisors


print(find_divisors(small_primes))


