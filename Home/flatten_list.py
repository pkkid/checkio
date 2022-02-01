#!/usr/bin/env checkio --domain=py run flatten-list

# https://py.checkio.org/mission/flatten-list/

# 
# END_DESC

#!/usr/bin/env checkio --domain=py run flatten-list
# https://py.checkio.org/mission/flatten-list/
#
# !!! Congratulation !!!
# Link for checking solution of other users: https://py.checkio.org/mission/flatten-list/publications/
# Link for sharing solution: https://py.checkio.org/mission/flatten-list/publications/add/

def flat_list(array):
    if isinstance(array, int):
        return [array]
    result = []
    for x in array:
        result += flat_list(x)
    return result


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')