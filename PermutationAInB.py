"""
Given two strings, A and B, check if any permutation of A exists in B.
ex.
A='bca'
B='catabcdog'

return True
"""

"""
permutation of A exists as sub sequence in B


strADict.get(k, dv)
"""
from collections import Counter


class Solution:

    def isPermuationAInB(A, B):
        # check length of string A can fit into B
        if len(A) > len(B):
            return False

        # strATally = Counter()
        # for c in list(A):
        #     strATally[c] += 1

        strATally = Counter(A)

        tempTally = Counter(strATally)
        isFound = False

        for i, c in enumerate(B):
            # check length of string A can fit into the remainder of B
            if len(tempTally) > len(B) - i:
                break

            if c not in tempTally:
                tempTally = Counter(strATally)

            tempTally[c] -= 1

            if tempTally[c] <= 0:
                del tempTally[c]

            if not tempTally:  # tempTally is Empty
                isFound = True

        return isFound

###############################################################################

import unittest


class Test_isPermuationAInB(unittest.TestCase):

    def setUp(self):
        pass

    def test_A_in_B(self):
        strA = 'bca'
        strB = 'catabcdog'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertTrue(Solution.isPermuationAInB(strA, strB))

    def test_A_not_in_B(self):
        strA = 'xyz'
        strB = 'catabcdog'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertFalse(Solution.isPermuationAInB(strA, strB))

    def test_A_with_multiple_characters_not_in_B(self):
        strA = 'bcaa'
        strB = 'catabcdog'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertFalse(Solution.isPermuationAInB(strA, strB))

    def test_A_with_multiple_characters_in_B(self):
        strA = 'bcaa'
        strB = 'catabcadog'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertTrue(Solution.isPermuationAInB(strA, strB))

    def test_len_A_greater_than_len_B(self):
        strA = 'catabcdog'
        strB = 'bcaa'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertFalse(Solution.isPermuationAInB(strA, strB))

    def test_len_A_eq_len_B_fencepost(self):
        strA = 'bcaa'
        strB = 'aabc'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertTrue(Solution.isPermuationAInB(strA, strB))

    def test_len_A_ne_len_B_by_1_fencepost(self):
        strA = 'bca'
        strB = 'aabc'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertTrue(Solution.isPermuationAInB(strA, strB))

    def test_A_with_multiple_characters_len_A_eq_len_B_fencepost(self):
        strA = 'bcaa'
        strB = 'dabc'
        # print(Solution.isPermuationAInB(strA, strB))
        self.assertFalse(Solution.isPermuationAInB(strA, strB))


if __name__ == '__main__':
        unittest.main()
