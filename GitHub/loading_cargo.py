#!/home/mjs7231/.local/bin/checkio --domain=py run loading-cargo

# https://py.checkio.org/mission/loading-cargo/

# "Look Stephen, here's a list of the items that need to be loaded onto the ship. We're going to need a lot of        batteries." Nikola handed him a notepad.
# 
# "What are the numbers next to the items?"
# 
# "That is the weight of each item."
# 
# "Er, why?"
# 
# "So you can see how much your trading cards and comic book collection will weigh us down during flight." Rang        Sofias voice from the phone tube.
# 
# "What is she talking about?” asked Nikola “Ooooh, nevermind, that was sarcasm. It’s important because your        load-stabilizing belt is broken and there is no way that we can find a new one right now. That’s why, when you        carry the things on the list, you’ll have to redistribute their weights in order to get the minimal weight in        each arm."
# 
# "Okay, so I have to figure out how many batteries I should hold in each hand to prevent them from breaking when        they inevitably fall to the ground. Got it."
# 
# You have been given a list of integer weights.    You should help Stephen distribute these weights into two sets,    such that the difference between the total weight of each set is as low as possible.
# 
# Input data:A list of the weights as a list of integers.
# 
# Output data:The number representing the lowest possible weight difference as a positive integer.
# 
# Precondition:
# 0 < len(weights) ≤ 10
# all(0 < x < 100 for x in weights)
# 
# 
# END_DESC

def checkio(stones):
    mindiff = None
    for order in itertools.permutations(stones, len(stones)):
        for offset in range(0, len(stones)):
            pile1 = order[:offset]
            pile2 = order[offset:]
            diff = int(math.fabs(sum(pile1) - sum(pile2)))
            if mindiff is None or diff < mindiff:
                mindiff = diff
            if mindiff == 0: break
        if mindiff == 0: break
    return mindiff


if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print('All is ok')