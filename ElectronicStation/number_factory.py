#!/usr/bin/env checkio --domain=py run number-factory

# https://py.checkio.org/mission/number-factory/

# You are given a two or more digits numberN.    For this mission, you should find the smallest positive number ofX,    such that the product of its digits is equal to N.    If X does not exist, then return 0.
# 
# Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit.    Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.
# 
# Hints:Remember prime numbers (numbers divisible by only one) and be careful with endless loops.
# 
# Input:A number N as an integer.
# 
# Output:The number X as an integer.
# 
# How it is used:This task will teach you how to work with numbers in code.    You can factorize numbers and reconstruct them into new numbers.    Of course you can solve this problem with brute force,    but is that the best way?    Numbers are the foundation of mathematics and programming.
# 
# Precondition:
# 9 < N < 105.
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run number-factory





















from functools import reduce
from itertools import product
DIGITS = "23456789"

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

def checkio(num):
    if len(str(num)) == 1: return num
    if is_prime(num): return 0
    for size in range(2, len(str(num)) + 2):
        for test in product(DIGITS, repeat=size):
            result = reduce(lambda x,y: int(x)*int(y), test[1:], test[0])
            if result == num:
                return int("".join(sorted(test)))
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
    assert checkio(560) == 2578, "6th example"