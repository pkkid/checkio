#!/home/mjs7231/.local/bin/checkio --domain=py run merge-intervals

# https://py.checkio.org/mission/merge-intervals/

# You are given a sequence of intervals, as tuples of ints where the tuples are sorted by  their first element in ascending order.
# It is your task to minimize the number of intervals by merging those that intersect or  by removing intervals fitting into another one.
# 
# Since the range of values for the intervals is restricted to integers, you must also  merge those intervals between which no value can be found.
# 
# An example:
# Let's say you've got these 5 intervals:1..6, 3..5, 7..10, 9..12 and 14..16.1..6 and 3..5
# 3..5fits into1..6, so3..5must disappear.1..6 and 7..10
# Even though the intervals do not intersect, there can not be a value of type int      between them, so they have to be merged to the new interval1..10.1..10 and 9..12
# These intervals do intersect, because9 < 10,      so they have to be merged to the new interval1..12.1..12 and 14..16
# These two intervals do not intersect, so they must not be merged.So the intervals to be returned are:
# 1..12 and 14..16
# 
# Input:A sequence of intervals as a  list of tuples of 2 ints, sorted by their first element.
# 
# Output:The merged intervals as a list of tuples of 2 ints, sorted by their first element.
# 
# 
# END_DESC

"""
You are given a sequence of intervals, as tuples of ints where the tuples are
sorted by  their first element in ascending order. It is your task to minimize
the number of intervals by merging those that intersect or by removing intervals
fitting into another one.

Since the range of values for the intervals is restricted to integers, you must
also merge those intervals between which no value can be found.

An example:
Let's say you've got these 5 intervals: 1..6, 3..5, 7..10, 9..12, 14..16.
1..6 and 3..5 3..5 fits into 1..6, so 3..5 must disappear.1..6 and 7..10 Even though
the intervals do not intersect, there can not be a value of type int between them,
so they have to be merged to the new interval1..10.1..10 and 9..12
These intervals do intersect, because9 < 10, so they have to be merged to the
new interval1..12.1..12 and 14..16 These two intervals do not intersect, so they
must not be merged.So the intervals to be returned are:
1..12 and 14..16

Input:A sequence of intervals as a  list of tuples of 2 ints, sorted by their first element.
Output:The merged intervals as a list of tuples of 2 ints, sorted by their first element.
"""



def merge_intervals(intervals):
    nums = set()
    result = [[None, None]]
    for x,y in intervals:
        for i in range(x,y+1):
            nums.add(i)
    if not nums: return []
    for i in range(min(nums), max(nums)+1):
        if i not in nums and result[-1][1] is not None:
            result.append([None, None])
        elif i in nums and result[-1][0] is None:
            result[-1][0] = i
        elif i in nums and result[-1][0] is not None:
            result[-1][1] = i
    return [tuple(r) for r in result]


if __name__ == '__main__':
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')