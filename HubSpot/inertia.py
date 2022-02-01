#!/home/mjs7231/.local/bin/checkio --domain=py run inertia

# https://py.checkio.org/mission/inertia/

# This mission is an adaptation of the "Inertia" game (fromSimon Tatham's Portable Puzzle Collection).	If you are lost or just want to play, the game is availablehere.
# 
# You're on a rectangular mined icefield: when you go in one direction,	you slide on the ice until you're stopped by a rock, the end of the icefield,	or some rough spot. But you're here for a good reason,there are gems	on the icefield: you have to find any route to collect them all,	avoiding the mines.
# 
# The icefield will be represented by a tuple of strings. Gems will be represented	by '$', rocks by 'X', mines by '*', ice by ' ' and rough spots by '.'.
# 
# You can go in all eight directions: northwest 'NW', north 'N', northeast 'NE',	west 'W', east 'E', southwest 'SW', south 'S', southeast 'SE'.
# 
# Input:A tuple of strings and a tuple of two ints.
# 
# Output:An iterable of strings.
# 
# Preconditions:You can collect all gems in any possible order		(otherwise it would be far more difficult).Given puzzles are solvable.5 ≤ len(grid) ≤ 50 and 5 ≤ len(grid[0]) ≤ 50.all(len(row) == len(grid[0]) for row in grid).
# 
# 
# END_DESC

from typing import Tuple, Iterable

def inertia(grid: Tuple[str], start: tuple) -> Iterable[str]:
    # your code here


if __name__ == '__main__':
    def checker(function, grid, start):
        result = function(grid, start)
        GEM, ROUGH, ICE, ROCK, MINE = '$. X*'
        MOVES = {'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
                  'W': ( 0, -1),                'E': ( 0, 1),
                 'SW': ( 1, -1), 'S': ( 1, 0), 'SE': ( 1, 1)}
        grid, (x, y) = list(map(list, grid)), start
        nb_rows, nb_cols = len(grid), len(grid[0])
        for nb, move in enumerate(result, 1):
            try:
                dx, dy = MOVES[move]
            except KeyError:
                print(f"I don't understand your {nb}-th move: '{move}'.")
                return False
            while 0 <= x + dx < nb_rows and 0 <= y + dy < nb_cols and \
                  grid[x + dx][y + dy] != ROCK:
                x, y = x + dx, y + dy
                if grid[x][y] == ROUGH:
                    break
                elif grid[x][y] == GEM:
                    grid[x][y] = ICE
                elif grid[x][y] == MINE:
                    print(f"You are dead at {(x, y)}, bye!")
                    return False
        try:
            coord = next((i, j) for i, row in enumerate(grid)
                                for j, cell in enumerate(row) if cell == GEM)
        except StopIteration:
            print(f"Great, you did it in {nb} moves!")
            return True
        print(f"You have at least forgot one gem at {coord}.")
        return False

    GRIDS = (('5x5', (1, 1), ('*X$$.',
                              ' .$*.',
                              '... X',
                              ' *$* ',
                              'XXX*$')),

             ('7x6', (6, 1), ('**$.  ',
                              '$*$.. ',
                              'X.**.$',
                              '*XX$ .',
                              '.X  XX',
                              'X$* X$',
                              '$.*  .')),

             ('5x10', (3, 8), (' X**$X.$X*',
                               '*$ X$.X*$.',
                               '* *X$..$$X',
                               '*.  .* *. ',
                               'X.$.XX $ .')))

    for dim, start, grid in GRIDS:
        assert checker(inertia, grid, start), f'You failed with the grid {dim}.'

    print('The local tests are done. Click on "Check" for more real tests.')