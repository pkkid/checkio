# https://py.checkio.org/mission/probably-dice/

# You're on your way to a board game convention. Chances are there’ll be some
# stiff competition, so you decide to learn more about dice probabilities since
# you suspect you'll be rolling a lot of them soon.
# 
# Typically, when using multiple dice, you simply roll them and sum up all the
# result. To get started with your investigation of dice probability, write a
# function that takes the number of dice, the number of sides per die and a target
# number and returns the probability of getting a total roll of exactly the target
# value.    The result should be given with four digits precision as ±0.0001.
# For example, if you roll 2 six-sided dice, the probability of getting exactly a
# 3 is 2/36 or 5.56%,    which you should return as ≈0.0556.
# 
# For each test, assume all the dice are the same and are numbered from 1 to
# the number of sides, inclusive. So a 4-sided die (D4)  would have an equal chance
# of rolling a 1, 2, 3 or 4.    A 20-sided die (D20) would have an equal chance
# of rolling any number from 1 to 20.
# 
# Tips: Be careful if you want to use a brute-force solution -- you could have a
#  very, very long wait for edge cases.
# Input: Three arguments. The number of dice, the number of sides per die and
#  the target number as integers.
# Output: The probability of getting exactly target number on a single roll of
#  the given dice as a float.
# 
# Preconditions:
#  1 ≤dice_number≤ 10
#  2 ≤sides≤ 20
#  0 ≤target< 1000
# 
from collections import Counter
from itertools import combinations_with_replacement
from math import factorial


def probability(num_dice, num_sides, target):
    # find unique ways to roll target
    unique_rolls = []
    sides = range(1, num_sides+1)
    for roll in combinations_with_replacement(sides, num_dice):
        if sum(roll) == target:
            unique_rolls.append(roll)
    # find number of ways to roll each unique roll
    total_rolls = 0
    for roll in unique_rolls:
        denom = 1
        counts = Counter(roll)
        for count in counts.values():
            denom = denom * factorial(count)
        total_rolls = total_rolls + factorial(num_dice) / denom
    return round(total_rolls / (num_sides ** num_dice), 4)


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"