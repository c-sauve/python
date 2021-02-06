'''
Problem #9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

A little bit of extra info:
A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2.
Such a triple is commonly written (a, b, c), and a well-known example is (3, 4, 5).
If (a, b, c) is a Pythagorean triple, then so is (ka, kb, kc) for any positive integer k.
A primitive Pythagorean triple is one in which a, b and c are coprime
 (that is, they have no common divisor larger than 1).[1]
 A triangle whose sides form a Pythagorean triple is called a Pythagorean triangle, and is necessarily a right triangle.
'''

'''
a + b + c = 1000
a**2 + b**2 = c**2
1000 - c = a + b
'''
import math
value = 1000
for a in range(1, value):
    for b in range(2, value):
        ab = (a**2 + b**2)
        c = math.sqrt(ab)
        if (a + b + c) == value:
            print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))
            print(str(a) + " + " + str(b) + "+" + str(c) + "=" + str(a + b + c))
            print("The product of abc = " + str(a * b * c))
            break
