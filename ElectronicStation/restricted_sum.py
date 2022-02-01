#!/usr/bin/env checkio --domain=py run restricted-sum

# https://py.checkio.org/mission/restricted-sum/

# Our new calculator is censored and as such it does not accept certain words.    You should try to trick by writing a program to calculate the sum of numbers.
# 
# Given a list of numbers, you should find the sum of these numbers.    Your solution should not contain any of the banned words, even as a part of another word.
# 
# The list of banned words are as follows:
# 
# sumimportforwhilereduceInput:A list of numbers.
# 
# Output:The sum of numbers.
# 
# Precondition:The small amount of data. Let's creativity win!
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run restricted-sum
# https://py.checkio.org/mission/restricted-sum/

def _checkio(data, i, r):
    if i < len(data):
        r[0] += data[i]
        _checkio(data, i+1, r)
    return r[0]

def checkio(data):
    return _checkio(data, 0, [0])