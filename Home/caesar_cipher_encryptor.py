#!/usr/bin/env checkio --domain=py run caesar-cipher-encryptor

# https://py.checkio.org/mission/caesar-cipher-encryptor/

# This mission is the part of the set. Another one -Caesar cipher decriptor.
# 
# Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
# 
# 
# 
# Input:A secret message as a string (lowercase letters only and white spaces)
# 
# Output:The same string, but encrypted
# 
# Precondition:
# 0<len(text)<50
# -26<delta<26
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run caesar-cipher-encryptor















ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def to_encrypt(text, delta):
    result = ''
    for c in text:
        result += ALPHA[(ALPHA.index(c) + delta) % len(ALPHA)] if c in ALPHA else c
    return result


if __name__ == '__main__':
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"