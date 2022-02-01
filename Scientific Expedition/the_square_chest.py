#!/usr/bin/env checkio --domain=py run the-square-chest

# https://py.checkio.org/mission/the-square-chest/

# On the chest keypad is a grid of numbered dots.    The grid is comprised of a square shaped array of dots and contains lines    that connect some pairs of adjacent dots.    The answer to the code is the number of squares that are formed by these lines.    For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.
# 
# 
# 
# The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented by lists of two numbers.
# 
# Input:A list of lines as a list of list. Each list consists of the two integers.Output:The quantity of squares formed as an integer.
# END_DESC

#!/usr/bin/env checkio --domain=py run the-square-chest












small = lambda n: [[n,n+1], [n+1,n+5], [n+4,n+5], [n,n+4]]
medium = lambda n: [[n,n+1], [n+1,n+2], [n+2,n+6], [n+6,n+10], [n+9,n+10], [n+8,n+9], [n+4,n+8], [n,n+4]]
large = lambda: [[1,2],[2,3],[3,4],[4,8],[8,12],[12,16],[15,16],[14,15],[13,14],[9,13],[5,9],[1,5]]
SQUARES = [small(1), small(2), small(3), small(5), small(6), small(7), small(9), small(10), small(11),
    medium(1), medium(2), medium(5), medium(6), large()]

def checkio(lines):
    lines = [sorted(line) for line in lines]
    count = len(SQUARES)
    for square in SQUARES:
        for line in square:
            if line not in lines:
                count -= 1
                break
    return count


if __name__ == '__main__':
    assert (checkio([[1,2],[3,4],[1,5],[2,6],[4,8],[5,6],[6,7],
        [7,8],[6,10],[7,11],[8,12],[10,11],[10,14],[12,16],
        [14,15],[15,16]]) == 3) , "First, from description"
    assert (checkio([[1,2],[2,3],[3,4],[1,5],[4,8],[6,7],[5,9],
        [6,10],[7,11],[8,12],[9,13],[10,11],[12,16],[13,14],
        [14,15],[15,16]]) == 2), "Second, from description"
    assert (checkio([[1,2],[1,5],[2,6],[5,6]]) == 1), "Third, one small square"
    assert (checkio([[1,2],[1,5],[2,6],[5,9],[6,10],[9,10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16,15],[16,12],[15,11],[11,10],[10,14],
        [14,13],[13,9]]) == 0), "Fifth, snake"