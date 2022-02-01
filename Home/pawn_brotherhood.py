#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

#!/usr/bin/env checkio --domain=py run pawn-brotherhood






def safe_pawns(pawns):
    safe_pawns = 0
    for p in pawns:
        guard1 = '%s%s' % (chr(ord(p[0])-1), int(p[1])-1)
        guard2 = '%s%s' % (chr(ord(p[0])+1), int(p[1])-1)
        safe_pawns += 1 if (guard1 in pawns or guard2 in pawns) else 0
    return safe_pawns


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")