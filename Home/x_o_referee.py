#!/usr/bin/env checkio --domain=py run x-o-referee

# https://py.checkio.org/mission/x-o-referee/

# Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players    (X and O) who take turns marking the spaces in a 3×3 grid.    The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and    NE-SW) wins the game.
# 
# But we will not be playing this game. You will be the referee for this games results. You are given a result of a    game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to    return "X"    if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
# 
# 
# 
# A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
# 
# Input:A game result as a list of strings (unicode).
# 
# Output:"X", "O" or "D" as a string.
# 
# Precondition:
# There is either one winner or a draw.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run x-o-referee























LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def checkio(game):
    game = "".join(game)
    for line in LINES:
        result = "".join([game[p] for p in line])
        if result == "XXX": return "X"
        if result == "OOO": return "O"
    return "D"

if __name__ == '__main__':
    assert checkio(["X.O","XX.","XOO"]) == "X", "Xs wins"
    assert checkio(["OO.","XOX","XOX"]) == "O", "Os wins"
    assert checkio(["OOX","XXO","OXX"]) == "D", "Draw"