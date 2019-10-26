class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"

from bisect import (
    bisect_left,
    bisect_right
    )

def find_range(input_list, input_number):
    l = bisect_left(input_list, input_number)
    h = bisect_right(input_list, input_number) - 1

    return Range(l, h)

print(find_range([1,2,5,5,8,8,10], 8))
print(find_range([1,2,5,5,8,8,10], 2))
print(find_range([1,2,5,5,8,8,10], 5))

