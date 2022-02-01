#!/usr/bin/env checkio --domain=py run long-repeat-inside
# https://py.checkio.org/mission/long-repeat-inside/
# 
# There are four substring missions that were born all in one day and you
# shouldn’t be needed more than one day to solve them. All of those mission can
# be simply solved by brute force, but is it always the best way to go? (you might
# not have access to all of those missions yet, but they are going to be
# available with more opened islands on the map). It is the fourth and the last
# mission of the series. But if in the first mission you needed to find repeating
# letters, then in this one you should find a repeating sequence inside the
# substring. I have an example for you: in a string 'abababc' - 'ab' is a sequence
# that repeats more than once, so the answer will be 'ababab'
# 
# Input:String.Output:String.

def repeat_inside(line):
    return line

if __name__ == '__main__':
    assert repeat_inside('aaaaa') == 'aaaaa', 'First'
    assert repeat_inside('aabbff') == 'aa', 'Second'
    assert repeat_inside('aababcc') == 'abab', 'Third'
    assert repeat_inside('abc') == '', 'Forth'
    assert repeat_inside('abcabcabab') == 'abcabc', 'Fifth'
    print('All OK')