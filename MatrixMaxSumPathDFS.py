from collections import *

def matrix_max_sum_dfs_1(grid):
    if not grid or not grid[0] and not isinstance(grid[0], list):
        return 0
    if len(grid) < 2:
        if len(grid[0]) < 2:
            return grid[0][0]

    class TravelNode:
        def __init__(self, row, col, nodeSum, grid):
            self.row = row
            self.col = col
            nodeSum += grid[row][col]
            self.nodeSum = nodeSum
            
    maxSum = None
    maxRow = len(grid) - 1
    maxCol = len(grid[0]) - 1

    stack = []
    stack.append(TravelNode(0, 0, 0, grid))

    while stack:
        node = stack.pop()
        if node.row == maxRow and node.col == maxCol:
            if not maxSum or node.nodeSum > maxSum:
                maxSum = node.nodeSum
        else:
            if node.col < maxCol:
                stack.append(TravelNode(node.row, node.col+1, node.nodeSum, grid))
            if node.row < maxRow:
                stack.append(TravelNode(node.row+1, node.col, node.nodeSum, grid))

    return maxSum


###############################################################################

import unittest

class Test_matrix_max_sum_dfs_1(unittest.TestCase):

    def test_none(self):
        i = None
        e = 0
        self.assertEqual(matrix_max_sum_dfs_1(i), e)

    def test_empty(self):
        i = []
        e = 0
        self.assertEqual(matrix_max_sum_dfs_1(i), e)

    def test_invalidInput(self):
        i = [2]
        e = None
        with self.assertRaises(TypeError):
            matrix_max_sum_dfs_1(i)

    def test_single(self):
        i = [[2]]
        e = 2
        self.assertEqual(matrix_max_sum_dfs_1(i), e)

    def test_1(self):
        i = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        e = 29
        self.assertEqual(matrix_max_sum_dfs_1(i), e)

if __name__ == '__main__':
    unittest.main()
