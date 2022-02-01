#!/usr/bin/env checkio --domain=py run feed-pigeons

# https://py.checkio.org/mission/feed-pigeons/

# I start to feed one of the pigeons.    A minute later two more fly by and a minute after that another 3.    Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute,    but in case there's not enough food for all the birds, the pigeons who arrived first ate first.    Pigeons are hungry animals and eat without knowing when to stop.    If I haveNportions of bird feed, how many pigeons will be fed with at least one portion of wheat?
# 
# 
# 
# Input:A quantity of portions wheat as a positive integer.
# 
# Output:The number of fed pigeons as an integer.
# 
# Precondition:0 < N < 105.
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run feed-pigeons
















def checkio(food):
    pigeons = 0
    flock = 1
    while food > pigeons:
        pigeons += min(flock, food-pigeons)
        food -= pigeons
        flock += 1
    return pigeons


if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"