#!/usr/bin/env checkio --domain=py run open-labyrinth

# https://py.checkio.org/mission/open-labyrinth/

# "So, the Labyrinth is a piece of cake, is it? Well, let's see how you deal with this little        slice..."
# 
# Sarah: "You don't by any chance know the way through this labyrinth, do you?"
# The Worm: "Who, me? No, I'm just a worm. Say, come inside, and meet the missus"
# 
# "Labyrinth" (1986)
# 
# The labyrinth has no walls, but bushes surround the path on each side.    If a players move into a bush, they lose.    The labyrinth is presented as a matrix (a list of lists): 1 is a bush and 0 is part of the path.    The labyrinth's size is 12 x 12 and the outer cells are also bushes.    Players start at cell (1,1). The exit is at cell (10,10).    You need to find a route through the labyrinth.    Players can move in only four directions--South (down [1,0]), North (up [-1,0]),    East (right [0,1]), West (left [0, -1]).    The route is described as a string consisting of different characters:    "S"=South, "N"=North, "E"=East, and "W"=West.
# 
# Input:A labyrinth map as a list of lists with 1 and 0.
# 
# Output:The route as a string that contains "W", "E", "N" and "S".
# 
# Precondition:Outer cells are pits.
# len(labyrinth) == 12
# all(len(row) == 12 for row in labyrinth)
# 
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run open-labyrinth
























START, EXIT = (1,1),(10,10)
DIRECTIONS = {'S':(0,1), 'E':(1,0), 'N':(0,-1), 'W':(-1,0)}

def checkio(map):
    paths = {START: ""}             # Dict of {pos => path) for all current locations
    visited = set((START,))         # Set of all locations previously visited
    while EXIT not in visited:
        newpaths = {}
        for pos,path in paths.items():
            for dir,move in DIRECTIONS.items():
                newpos = (pos[0]+move[0], pos[1]+move[1])
                if (newpos not in visited) and (map[newpos[1]][newpos[0]] == 0):
                    visited.add(newpos)
                    newpaths[newpos] = path + dir
        paths = newpaths
    return paths[EXIT]


if __name__ == '__main__':
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    # Be carefull with infinity loop
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))