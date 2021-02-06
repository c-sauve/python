'''

# Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million (2,000,000).

I feel like i'm cheating a little bit here. Though it's okay to re-use code, I'm not re using code I create. :(
i'm using some code similar to the one I created. ( I found that code after I found the answer using my own code).
I'm referring to the code in 10001st prime.py
'''

counter = 2
set_number = 2000000
prime_numbers = []


def is_prime(value):
    if value == 1:
        return False
    elif value == 2:
        return True
    else:
        if value <= 100:
            for x in range(2, value):
                if value % x == 0:
                    return False

        for y in prime_numbers[0:round(len(prime_numbers) / 2)]:
            if value % 2 == 0:
                return False
            elif value % y == 0:
                return False
        return True


while len(prime_numbers) < set_number:
    if is_prime(counter):
        prime_numbers.append(counter)
        print(len(prime_numbers))
    counter += 1

print(prime_numbers[-1])
print("The sum of all the primes below two million is " + str(sum(prime_numbers)))


'''
So.. the above works.... it just takes A LONG TIME TO GET THE ANSWER like an hour probably... idk I stopped it half way
and used the below code. It was 30 + mins and not even half way done :,(,,
I googled some python librarys and found symPy. And OMG that just made this problem 100 EZ
CHECK THIS OUT!!!
'''
import sympy

prime_list = list(sympy.primerange(1, 2000000))
print(sum(prime_list))
