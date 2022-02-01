#!/home/mjs7231/.local/bin/checkio --domain=py run identify-block

# https://py.checkio.org/mission/identify-block/

# This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
# You are given 4 numbers(set of integer).These numbers represent the position of the square on the grid and one block if all the squares are adjacent.
# 
# You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
# The answer is an upper case alphabet ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it isn't a block then return None.
# 
# The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).
# 
# 
# 
# Input:4 numbers (set of integer)
# 
# Output:kind of the block (an alphabet or         None)
# 
# 
# END_DESC

N,S,E,W = (-1,0),(1,0),(0,1),(0,-1)
CHARS = {'I':[S,S,S], 'J':[S,S,W], 'L':[S,S,E], 'O':[S,E,N], 'S':[E,W,S,W], 'T':[E,E,W,S], 'Z':[E,S,E]}
move = lambda p, dir: [p[0]+dir[0], p[1]+dir[1]]
inbound = lambda p: 0 <= p[0] <= 3 and 0 <= p[1] <= 3
gridvalue = lambda grid, p: 1 if inbound(p) and grid[p[0]][p[1]] else 0

def _create_grid(numbers):
    grid = [[0]*4 for _ in range(4)]
    for num in numbers:
        row = int((num-1)/4)
        col = num-(row*4)-1
        grid[row][col] = 1
    return grid

def _get_start(grid):
    for pos in [(x,y) for x in range(4) for y in range(4)]:
        if gridvalue(grid, pos):
            return pos

def identify_block(numbers):
    grid = _create_grid(numbers)
    for i in range(4):
        for char,path in CHARS.items():
            pos, count = _get_start(grid), 0
            for dir in path:
                pos = move(pos, dir)
                count += gridvalue(grid, pos)
            if count == len(path):
                return char
        grid = list(zip(*reversed(grid)))
    return None

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) is None, 'None'
    print('"Run" is good. How is "Check"?')