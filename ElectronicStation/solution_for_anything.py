#!/usr/bin/env checkio --domain=py run solution-for-anything
# https://py.checkio.org/mission/solution-for-anything/
# 
# We need a solution which can pass any case. The result of your solution
# should pass for any comparison with anything. You should write the function
# "checkio" which is called with one argument, the result will be compared with
# some other data (==, !=, etc) and the result of that comparison should be True.
# 
# Input:Some data. Maybe that data over there.
# Output:The something as a something-else.


class Foo:
    #def __cmp__(self): return 0
    def __eq__(self, o): return True
    def __gt__(self, o): return True
    def __lt__(self, o): return True
    def __ne__(self, o): return True
    def __le__(self, o): return True
    def __ge__(self, o): return True


def checkio(anything):
    """ try to return anything else :) """
    return Foo()

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')