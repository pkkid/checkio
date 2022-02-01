#!/usr/bin/env checkio --domain=py run most-wanted-letter

# https://py.checkio.org/mission/most-wanted-letter/

# You are given a text, which contains different english letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

#!/usr/bin/env checkio --domain=py run most-wanted-letter



















from collections import defaultdict
ALPHA = "abcdefghijklmnopqrstuvwxyz"

def checkio(text):
    letters = defaultdict(int)
    for char in text:
        if char in ALPHA:
            letters[char.lower()] += 1
    return sorted(letters.items(), key=lambda x: (-x[1], x[0]))[0][0]

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."