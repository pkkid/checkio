#!/usr/bin/env checkio --domain=py run long-repeat

# https://py.checkio.org/mission/long-repeat/

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.
# 
# Input:String.Output:Int.
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run long-repeat
















def long_repeat(line):
    if not line:
        return 0
    cur = [1, line[0]]
    max = [1, line[0]]
    for c in line[1:]:
        if c != cur[1]:
            if cur > max:
                max = cur
            cur = [1, c]
        else:
            cur[0] += 1
    if cur > max:
        max = cur
    return max[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')