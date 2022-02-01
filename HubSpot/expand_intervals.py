#!/home/mjs7231/.local/bin/checkio --domain=py run expand-intervals

# https://py.checkio.org/mission/expand-intervals/

# An  interval of consecutive positive integers can be succinctly described as an tuple that contains first and last values. For example, the interval that contains the numbers 5, 6, 7, 8, 9 can be described as (5,9). Multiple intervals can be united together into iterable. Given an iterable with intervals (guaranteed not to overlap with each other and to be listed in sorted ascending order), create and return the list that contains all the integers contained by these intervals.
# 
# Input:Iterable of tuples of two integers.
# 
# Output:Iterable of integers.
# 
# Precondition:each element in the interval is a integer and
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# See also:Create IntervalsMerge Intervals
# 
# 
# END_DESC

from typing import Iterable

def expand_intervals(items: Iterable) -> Iterable:
    # your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")