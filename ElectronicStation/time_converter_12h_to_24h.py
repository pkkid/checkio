#!/home/mjs7231/.local/bin/checkio --domain=py run time-converter-12h-to-24h
# https://py.checkio.org/mission/time-converter-12h-to-24h/
# 
# You are the modern man who prefers the 24-hour time format. But the 12-hour
# format is used in some places. Your task is to convert the time from the 12-h
# format into 24-h by following the next rules:
# - the output format should be 'hh:mm'
# - if the output hour is less than 10 - write '0' before it. For example: '09:05'
# 
# Input:Time in a 12-hour format (as a string).
# Output:Time in a 24-hour format (as a string).
# Precondition: '00:00'<= time<= '23:59'

def time_converter(time):
    hourmin, am = time.split(' ')
    hour, min = [int(x) for x in hourmin.split(':')]
    hour += 12 if am == 'p.m.' else 0
    if hour == 12: hour = 0
    if hour == 24: hour = 12
    return '{:0>2}:{:0>2}'.format(hour, min)

if __name__ == '__main__':
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
