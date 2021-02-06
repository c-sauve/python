'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

prime_numbers = [2, 3, 5, 7, 11]
def get_prime_number(value):
    array = []
    for numbers in range(value):
        if numbers > 2:
            if value % numbers == 0:
                array.append(round(value/numbers))
    return array


def is_prime_number(value):
    if (value - 1)%6 == 0:
        return True
    elif value in prime_numbers:
        return True
    return False


value = 600851475143
value = 20
winner = 0
cont = True
while cont:
    for numbers in range(value):
        if numbers > 0:
            if value % numbers == 0:
                if is_prime_number(value) & is_prime_number(numbers):
                    winner = value
                    cont = False
                    break
                else:
                    winner = value
                    value = (round(value/numbers))
                    print(numbers)
                    print(value)
                    if value in prime_numbers:
                        winner = value
                        cont = False
                        break
                    elif value == 1:
                        cont = False
                        break

print(winner)
if winner % 2 == 0 and winner != 2:
    print("There are no prime factors other than 1")
else:
    print("The largest prime factor is " + str(winner))
