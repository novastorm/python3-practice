def findMinimumElement(a):
    if not a:
        return None
    if len(a) == 1 or a[0] < a[len(a)-1]:
        return a[0]

    lo = 0
    hi = len(a)-1

    while lo < hi and a[lo] > a[hi]:

        mid = (lo + hi) // 2
        if a[lo] <= a[mid]:
            lo = mid + 1
        else:
            hi = mid

    return a[lo]


###############################################################################

import unittest

class Test_BinaryTree_max_sum_path(unittest.TestCase):

    def test_empty(self):
        i = []
        e = None
        self.assertEqual(findMinimumElement(i), e)

    def test_1_element(self):
        i = [3]
        e = 3
        self.assertEqual(findMinimumElement(i), e)

    def test_odd_1(self):
        i = [5, 7, 10, 3, 4]
        e = 3
        self.assertEqual(findMinimumElement(i), e)

    def test_odd_2(self):
        i = [10, 3, 4, 5, 7]
        e = 3
        self.assertEqual(findMinimumElement(i), e)

    def test_odd_3(self):
        i = [4, 5, 7, 10, 3]
        e = 3
        self.assertEqual(findMinimumElement(i), e)

    def test_odd_4(self):
        i = [3, 4, 5, 7, 10]
        e = 3
        self.assertEqual(findMinimumElement(i), e)


if __name__ == '__main__':
    unittest.main()

