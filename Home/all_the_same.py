#!/usr/bin/env checkio --domain=py run all-the-same

# https://py.checkio.org/mission/all-the-same/

# In this mission you should check if all elements in the given list are equal.
# 
# Input:List.
# 
# Output:Bool.
# 
# The idea for this mission was found onPython Tricks series by Dan Bader
# 
# Precondition:all elements of the input list are hashable
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run all-the-same








from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for x in elements[1:]:
        if x != elements[0]:
            return False
    return True


if __name__ == '__main__':
    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True