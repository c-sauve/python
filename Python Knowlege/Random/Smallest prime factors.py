#!/usr/bin/python3
import sympy
# lets see if we can find the lowest prime factors for a number.

# This function will print out a list of all the smallest prime factors for a given number.


def find_smallest_primes(value):
    smallest_primes = []
    while not sympy.isprime(int(value)):
        if int(value) == 1:
            break
        for prime_numbers in sympy.primerange(1, value):
            if value % prime_numbers == 0:
                smallest_primes.append(prime_numbers)
                value /= prime_numbers
                print(int(value))
                if int(value) == 1:
                    break

    smallest_primes.append(int(value))

    return smallest_primes


value = 600851475143
print(find_smallest_primes(value))
