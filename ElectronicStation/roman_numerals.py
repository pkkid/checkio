#!/usr/bin/env checkio --domain=py run roman-numerals

# https://py.checkio.org/mission/roman-numerals/

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC

#!/usr/bin/env checkio --domain=py run roman-numerals






ROMANS = ((1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"),
    (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I"))

def checkio(number):
    result = ""
    for value, unit in ROMANS:
        count = int(number // value)
        result += unit * count
        number -= value * count
    return result

if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
    print('All ok')