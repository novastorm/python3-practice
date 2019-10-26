def print_paths(board):
    print_paths_iterative(board)


def print_paths_recursive(board):
    rows = len(board)
    cols = len(board[0])

    results = []
    temp = []

    def helper(r, c, board=board, temp=temp, results=results):
        if r >= rows or c >= cols:
            return

        temp.append(board[r][c])

        if r == rows - 1 and c == cols - 1:
            results.append("".join(temp))
            temp.pop()
            return

        helper(r + 1, c)
        helper(r, c + 1)
        temp.pop()

    helper(0, 0)

    return results


def print_paths_iterative(board):
    rows = len(board)
    cols = len(board[0])

    stack = [(0, 0, "")]

    results = []

    while stack:
        r, c, s = stack.pop()

        ch = board[r][c]

        if r == rows - 1 and c == cols - 1:
            results.append(s + ch)
            continue

        if c + 1 < cols:
            stack.append((r, c + 1, s + ch))
        if r + 1 < rows:
            stack.append((r + 1, c, s + ch))

    return results


##############################################################################

import unittest


M = 'matrix'
E = 'expected'

class Test_PrintMatrixPaths(unittest.TestCase):

    def setUp(self):

        self.inputs = [
            {
                M: [
                    ['A', 'X'],
                    ['B', 'E']
                ],
                E: set(['ABE', 'AXE'])
            },
            {
                M: [
                    ['A', 'B', 'C'],
                    ['D', 'E', 'F'],
                    ['G', 'H', 'I']
                ],
                E: set(['ADGHI', 'ADEHI', 'ADEFI', 'ABEHI', 'ABEFI', 'ABCFI'])
            },
            {
                M: [
                    ['A', 'B'],
                    ['D', 'E'],
                    ['G', 'H']
                ],
                E: set(['ADGH', 'ADEH', 'ABEH'])
            },
            {
                M: [
                    ['A', 'B', 'C'],
                    ['D', 'E', 'F']
                ],
                E: set(['ADEF', 'ABEF', 'ABCF'])
            }
        ]

    def test_print_paths_recursive(self):
        for t in self.inputs:
            m, e = t[M], t[E]
            self.assertEqual(set(print_paths_recursive(m)), e)

    def test_print_paths_iterative(self):
        for t in self.inputs:
            m, e = t[M], t[E]
            self.assertEqual(set(print_paths_iterative(m)), e)


if __name__ == '__main__':
    unittest.main()
