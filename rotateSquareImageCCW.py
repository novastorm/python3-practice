def rotate_square_image_ccw(matrix):
    return rotate_square_image_ccw_1(matrix)

def rotate_square_image_ccw_1(matrix):
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def flip_horizontal(matrix):
        for r in range(len(matrix)):
            i = 0
            j = len(matrix[r]) - 1
            while i < j:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
                i += 1
                j -= 1
    flip_horizontal(matrix)
    transpose(matrix)
    return matrix

def rotate_square_image_ccw_2(matrix):
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def flip_horizontal(matrix):
        for r in range(len(matrix)):
            for i in range(len(matrix[0]) // 2):
                j = len(matrix) - 1 - i 
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
    flip_horizontal(matrix)
    transpose(matrix)
    return matrix

def rotate_square_image_ccw_3(matrix):
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def flip_horizontal(matrix):
        for r in matrix:
            for i in range(len(matrix[0]) // 2):
                j = len(matrix) - 1 - i 
                r[i], r[j] = r[j], r[i]
    flip_horizontal(matrix)
    transpose(matrix)
    return matrix


def rotate_square_image_ccw_4(matrix):
    l = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(len(matrix) // 2):
            (   matrix[i][j], 
                matrix[l-j][i], 
                matrix[l-i][l-j], 
                matrix[j][l-i]) \
            = (
                matrix[l-j][i], 
                matrix[l-i][l-j], 
                matrix[j][l-i], 
                matrix[i][j])

    return matrix



###############################

import unittest

class Test_BinaryTree_max_sum_path(unittest.TestCase):

    I = 'input'
    E = 'expected'

    def setUp(self):
        I = self.I
        E = self.E
        self.tests = [
            {
                I: [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                E: [[3, 6, 9],
                    [2, 5, 8],
                    [1, 4, 7]]
            },
            {
                I: [[ 1,  2,  3,  4],
                    [ 5,  6,  7,  8],
                    [ 9, 10, 11, 12],
                    [13, 14, 15, 16]],
                E: [[ 4,  8, 12, 16],
                    [ 3,  7, 11, 15],
                    [ 2,  6, 10, 14],
                    [ 1,  5,  9, 13]]
            }
        ]

    def test_rotate_square_image_ccw_4(self):
        I = self.I
        E = self.E

        for t in self.tests:
            i, e = t[I], t[E]
        self.assertEqual(rotate_square_image_ccw(i), e)


if __name__ == '__main__':
    unittest.main()
