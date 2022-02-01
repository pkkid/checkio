#!/home/mjs7231/.local/bin/checkio --domain=py run speechmodule

# https://py.checkio.org/mission/speechmodule/

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
# 
# Input:A number as an integer.
# 
# Output:The string representation of the number as a string.
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

NUMBERS = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
    14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
    19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
    70:"seventy", 80:"eighty", 90:"ninety"
}

def _checkio(strnum, result):
    if not strnum or strnum in "00":
        return result
    if int(strnum) in NUMBERS:
        result.append(NUMBERS[int(strnum)])
        return _checkio("", result)
    if len(strnum) == 3:
        result.append(NUMBERS[int(strnum[0])])
        result.append("hundred")
        return _checkio(strnum[1:], result)
    result.append(NUMBERS[int("%s0" % strnum[0])])
    return _checkio(strnum[1:], result)
        
def checkio(number):
    if number == 0: return "zero"
    if number == 1000: return "one thousand"
    result = _checkio(str(number), [])
    return " ".join(result)

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=="two hundred twelve", "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"
    print('All ok')