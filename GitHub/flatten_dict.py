#!/usr/bin/env checkio --domain=py run flatten-dict

# https://py.checkio.org/mission/flatten-dict/

# 
# END_DESC

#!/usr/bin/env checkio --domain=py run flatten-dict


# Done!


def flatten(data, path='', result=None):
    result = result or {}
    for key, value in data.items():
        value = value or ''
        newpath = '%s/%s' % (path, key) if path else key
        if isinstance(value, dict):
            result = flatten(value, newpath, result)
        else:
            result[newpath] = value
    return result


if __name__ == '__main__':
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')