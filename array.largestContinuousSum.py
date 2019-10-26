import array


class Array(array.Array):

    @staticmethod
    def largestContinuousSum(arr):
        if not arr:
            return 0
            
        maxEndingHere = arr[0]
        maxSoFar = arr[0]

        for n in arr[1:]:
            maxEndingHere = max(maxEndingHere + n, n)
            maxSoFar = max(maxEndingHere, maxSoFar)

        return maxSoFar


###############################################################################

import unittest


class Test_BinaryTree_lowest_common_ancestor(unittest.TestCase):

    def test_largestContinuousSum(self):
        i = [-1, -2, 3, 4, 5]
        e = 12
        self.assertEqual(Array.largestContinuousSum(i), e)

    def test_largestContinuousSum(self):
        i = [1, 2, 3, -2, 5]
        e = 9
        self.assertEqual(Array.largestContinuousSum(i), e)

    def test_largestContinuousSum(self):
        i = [1, 2, 3]
        e = 6
        self.assertEqual(Array.largestContinuousSum(i), e)

    def test_largestContinuousSum(self):
        i = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
        e = 187
        self.assertEqual(Array.largestContinuousSum(i), e)

    def test_largestContinuousSum(self):
        i = [0, -2, -1, -3]
        e = 0
        self.assertEqual(Array.largestContinuousSum(i), e)

    def test_largestContinuousSum(self):
        i = [-8, -2, -1, -9, -2, -4]
        e = -1
        self.assertEqual(Array.largestContinuousSum(i), e)


if __name__ == '__main__':
        unittest.main()
