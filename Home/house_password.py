#!/usr/bin/env checkio --domain=py run house-password

# https://py.checkio.org/mission/house-password/

# 
# END_DESC

#!/usr/bin/env checkio --domain=py run house-password


DIGITS = "0123456789"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def contains_one(data, chars):
    for char in chars:
        if char in data:
            return True
    return False


def checkio(data):
    """ Password is considered to be strong enough if its length is more
        than or equal 10 symbols and it has at least one digit, one upper
        and one lower case letters.
    """
    if len(data) < 10: return False
    if not contains_one(data, ALPHA.upper()): return False
    if not contains_one(data, ALPHA.lower()): return False
    if not contains_one(data, DIGITS): return False
    return True


if __name__ == '__main__':
    assert checkio('A1213pokl') is False, 'First'
    assert checkio('bAse730onE4') is True, 'Second'
    assert checkio('asasasasasasasaas') is False, 'Third'
    assert checkio('QWERTYqwerty') is False, 'Fourth'
    assert checkio('123456123456') is False, 'Fifth'
    assert checkio('QwErTy911poqqqq') is True, 'Sixth'
    print('All ok')