# https://py.checkio.org/en/mission/shortest-knight-path/
# 
# Sofi found a chess set in the supply closet on the robots ship. She has
# decided to learn how to play the game of chess starts by attempting to
# understand how the knight moves.
# 
# Chess is played on a square board of eight rows (called ranks and denoted with
# numbers 1 to 8) and eight columns (called files and denoted with letters
# a to h) of squares. The knight moves to any of the closest squares that are
# not on the same rank, file, or diagonal, thus the move forms an "L"-shape: two
# squares vertically and one square horizontally, or two squares horizontally
# and one square vertically.
# 
# You are given the start and end squares as chess coordinates. You should find
# the length of the shortest path for the knight from one point to another on
# the chessboard.
# 
# Input: Squares coordinates as a string.
# Output: The number of moves in the shortest path the knight can take as an int.
# Precondition: start_cell != end_cell
#
MOVES = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
inbound = lambda p: 0 <= p[0] < 8 and 0 <= p[1] < 8
pos = lambda p: ('abcdefgh'.index(p[0]), int(p[1])-1)

def num_moves(start, end):
    moves = 0
    start, end = pos(start), pos(end)
    visited = set((start,))
    while len(visited) < 64:
        moves += 1
        for p in list(visited):
            newspots = ((p[0]+m[0], p[1]+m[1]) for m in MOVES)
            visited.update(filter(inbound, newspots))
            #if end in visited: break
    return moves

if __name__ == '__main__':
    print(num_moves('a1', 'a1'))

    with open('tests.txt', 'r') as f:
        for line in f.read().splitlines():
            start, end, num = line.split()

            assert num_moves(start, end) == int(num), "%s->%s = %s" % (start, end, num)
    print('All ok')
