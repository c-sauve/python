'''
Problem #7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

What is a prime number?
Prime numbers are numbers that have only 2 factors: 1 and themselves.
For example, the first 5 prime numbers are 2, 3, 5, 7, and 11. By contrast, numbers with more than 2 factors are call
    composite numbers.

'''

# Functions

'''
    The purpose of this function is to create a list of prime numbers, and return a number based on which prime number
        slot you're looking for.
    Parameter: 
        value -> This is suppose to be a non negative integer
    return:
        answer -> This will be a prime number in the n'th slot
        
   This function will take a very long to return the result if value > 5000
'''


def find_prime_number(value):
    last_known_value = 0
    if isinstance(value, int):
        prime_numbers = [2, 3, 5, 7, 11, 13]
        counter = 1
        while len(prime_numbers) <= value:
            counter += 1
            found_value = False

            for values in range(2, 1000):
                if counter in prime_numbers:
                    found_value = True
                    continue
                if counter == values:
                    prime_numbers.append(counter)
                if counter % values == 0:
                    found_value = True
                    break
            if not found_value:
                prime_numbers.append(counter)

            # This is a slower method to find larger prime numbers but works all the same.
            #for values in range(2, counter + 1):
            #    if counter in prime_numbers:
            #        continue
            #    if counter == values:
            #        prime_numbers.append(counter)
            #    if counter % values == 0:
            #        break

            if last_known_value != len(prime_numbers):
                last_known_value = len(prime_numbers)
                print(len(prime_numbers))

        answer = prime_numbers[value - 1]
        return answer
    else:
        print("Please use a non negative integer value")
        exit(1)


print(find_prime_number(10001))

'''
#This is a way better method found from the page. I was looking at other solutions after I used mine.


def test_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if n % x==0:
                return False
        return True


list1 = list()
a=2

while len(list1) < 10001:
    if test_prime(a):
        list1.append(a)
        print(len(list1))
    a+=1



print(list1[-1])
'''
