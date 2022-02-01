#!/usr/bin/env checkio --domain=py run largest-histogram
# https://py.checkio.org/mission/largest-histogram/
# 
# You have a histogram. Try to find size of the biggest rectangle you can build
# out of the histogram bars.
# 
# Input: List of all rectangles heights in histogram
# Output: Area of the biggest rectangle
# 
# How it is used: There is no way the solution you come up with will be any
# useful in a real life. Just have some fun here.
# 
# Precondition:
# 0 < len(data) < 1000

def largest_histogram(hist):
    max_area = 0
    for x1, col in enumerate(hist):
        for height in range(1, col+1):
            x2 = x1
            while x2 < len(hist) and hist[x2] >= height:
                x2 += 1
            max_area = max(max_area, (x2 - x1) * height)
    return max_area


if __name__ == "__main__":
    # assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")