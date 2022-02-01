#!/usr/bin/env checkio --domain=py run morse-clock

# https://py.checkio.org/mission/morse-clock/

# 
# END_DESC

#!/usr/bin/env checkio --domain=py run morse-clock






PADS = "24:34:34"

def checkio(data):
    result = ""
    data = ":".join(s.zfill(2) for s in data.split(":"))
    for i in range(len(data)):
        if data[i] == ":":
            result += ": "
        else:
            binary = bin(int(data[i]))[2:].zfill(int(PADS[i]))
            result += "%s " % binary.replace("0", ".").replace("1", "-")
    return result.strip()

if __name__ == "__main__":    
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("11:10:12") == ".- ...- : ..- .... : ..- ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"