class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"


class ListOfRangeIterator:

    def __init__(self, aList):
        self.aList = aList

    def __iter__(self):
        return self

    def __next__(self):
        if not self.aList:
            raise StopIteration

        next = self.aList.pop(0)

        return (next.lower_bound, next.upper_bound)

    next = __next__


def merge_ranges(input_range_list):
    if not input_range_list or len(input_range_list) < 2:
        return input_range_list
        
    results = [input_range_list[0]]

    for r in input_range_list:
        if r.lower_bound <= results[-1].upper_bound:
            results[-1].upper_bound = r.upper_bound
        else:
            results.append(r)

    return results


###############################################################################

import unittest


class Test_merge_ranges_1(unittest.TestCase):

    def test_1(self):
        l = [Range(1, 10), Range(5, 8), Range(8, 15)]
        lm = merge_ranges(l)
        i = list(iter(ListOfRangeIterator(lm)))

        b = [Range(1, 15)]
        e = list(iter(ListOfRangeIterator(b)))

        self.assertEqual(i, e)

    def test_2(self):
        l = [Range(5, 50), Range(25, 100), Range(150, 200)]
        lm = merge_ranges(l)
        i = list(iter(ListOfRangeIterator(lm)))

        b = [Range(5, 100), Range(150, 200)]
        e = list(iter(ListOfRangeIterator(b)))

        self.assertEqual(i, e)

    def test_3(self):
        l = [Range(1, 4), Range(3, 7), Range(5, 10), Range(11, 15)]
        lm = merge_ranges(l)
        i = list(iter(ListOfRangeIterator(lm)))

        b = [Range(1, 10), Range(11, 15)]
        e = list(iter(ListOfRangeIterator(b)))

        self.assertEqual(i, e)

    def test_4(self):
        l = [Range(1, 5), Range(5, 10), Range(11, 15), Range(15, 20)]
        lm = merge_ranges(l)
        i = list(iter(ListOfRangeIterator(lm)))

        b = [Range(1, 10), Range(11, 20)]
        e = list(iter(ListOfRangeIterator(b)))

        self.assertEqual(i, e)

    def test_5(self):
        l = [Range(1, 2), Range(2, 5), Range(8, 10), Range(15, 20)]
        lm = merge_ranges(l)
        i = list(iter(ListOfRangeIterator(lm)))

        b = [Range(1, 5), Range(8, 10), Range(15, 20)]
        e = list(iter(ListOfRangeIterator(b)))

        self.assertEqual(i, e)

if __name__ == '__main__':
    unittest.main()