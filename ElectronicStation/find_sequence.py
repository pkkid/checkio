#!/usr/bin/env checkio --domain=py run find-sequence

# https://py.checkio.org/mission/find-sequence/

# “There’s nothing here...” sighed Nikola.
# 
# “You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” SaidSofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
# 
# “Where did you get-”
# 
# “Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
# 
# CLUNK
# 
# “Hey we hit something.” Stephen exclaimed in surprise.
# 
# “It’s the treasure!” Sofia was jumping up and down in excitement.
# 
# The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing        the lid but it was locked. Nikola studied the locking mechanism.
# 
# “I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4        or more matching numbers and output a bool.”
# 
# “Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.
# 
# You are given a matrix of NxN (4≤N≤10).    You should check if there is a sequence of 4 or more matching digits.    The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
# 
# Input:A matrix as a list of lists with integers.
# 
# Output:Whether or not a sequence exists as a boolean.
# 
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run find-sequence




































DIRS = ((0,1), (1,1), (1,0))
value = lambda pos,map: map[pos[0]][pos[1]]

def sequence(pos, dir, map):
    inbound = lambda pos: 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])
    for newpos in ((pos[0]+dir[0]*i,pos[1]+dir[1]*i) for i in range(1,4)):
        if not inbound(newpos) or value(pos, map) != value(newpos, map):
            return False
    return True

def checkio(map):
    for pos in ((x,y) for x in range(len(map)) for y in range(len(map[0]))):
        if any((sequence(pos, dir, map) for dir in DIRS)):
            return True
    return False


if __name__ == '__main__':
    assert checkio([
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "First, horizontal"
    assert checkio([
        [7, 6,  5, 7, 9],
        [8, 7,  3, 6, 5],
        [4, 0,  6, 5, 4],
        [9, 8,  4, 0, 5],
        [2, 10, 7, 2, 10]
    ]) == False, "Second"
    assert checkio([
        [10, 1, 9,  6, 4, 1],
        [2,  5, 4,  2, 2, 7],
        [2,  2, 1,  2, 6, 4],
        [3,  2, 2,  1, 0, 2],
        [7,  9, 6,  2, 5, 7],
        [7,  3, 10, 5, 6, 2]
    ]) == True, "Third"
    assert checkio([
        [6, 6, 7, 7, 7],
        [1, 7, 3, 6, 5],
        [4, 1, 2, 3, 2],
        [9, 0, 4, 0, 5],
        [2, 0, 7, 5, 10]
    ]) == False, "fourth"
    assert checkio([
        [1,  1, 1,  6, 1, 1, 1],
        [2,  5, 4,  2, 2, 7, 2],
        [2,  6, 1,  2, 6, 4, 3],
        [3,  2, 2,  1, 0, 2, 4],
        [7,  9, 6,  2, 5, 7, 5],
        [7,  3, 10, 5, 6, 2, 5],
        [7,  3, 10, 5, 6, 2, 5]
    ]) == False, "Fifth"
    assert checkio([
        [1, 1, 3, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "Six, vertircal"
    print("All ok")