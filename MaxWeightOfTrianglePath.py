'''
This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''

class Solution:

    def get_left_index(r, c):
        return r + 1, c

    def get_right_index(r, c):
        return r + 1, c + 1

    def get_max_weight_path_top_down_recursive(self, root, r=0, c=0):
        if not root:
            return None
        if r < 0 or r >= len(root) or c >= len(root[r]):
            print r, c
            raise ValueError

        max_left = 0
        max_right = 0

        if r < len(root) - 1:
            max_left = self.get_max_weight_path_top_down_recursive(root, r+1, c)
            max_right = self.get_max_weight_path_top_down_recursive(root, r+1, c+1)

        return root[r][c] + max(max_left, max_right) 


###############################################################################

import unittest


class Test_get_max_weight_path_1(unittest.TestCase):

    f = Solution().get_max_weight_path_top_down_recursive

    def test_None(self):
        i = None
        e = None
        self.assertEqual(self.f(i), e)

    def test_Empty(self):
        i = []
        e = 0
        self.assertEqual(self.f(i), e)

    def test_0(self):
        i = [[1], [2, 3], [1, 5, 1]]
        e = 9, # [1, 3, 5]
        self.assertEqual(self.f(i), e)


if __name__ == '__main__':
    unittest.main()
