def find_spiral(matrix):
    return find_spiral_1(matrix)


def find_spiral_1(matrix):
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return []

    def N(r, c):
        return r - 1, c

    def S(r, c):
        return r + 1, c

    def W(r, c):
        return r, c - 1

    def E(r, c):
        return r, c + 1

    minR = 0
    maxR = len(matrix) - 1
    minC = 0
    maxC = len(matrix[0]) - 1

    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    dirTable = [E, S, W, N]

    results = []

    r = 0
    c = 0

    d = 0

    def isValidDir(r, c):
        return minR <= r <= maxR and minC <= c <= maxC

    while minR <= maxR and minC <= maxC:
        results.append(matrix[r][c])
        newR, newC = dirTable[d](r, c)
        if isValidDir(newR, newC):
            r, c = newR, newC
        else:
            if d == EAST:
                minR += 1
            if d == SOUTH:
                maxC -= 1
            if d == WEST:
                maxR -= 1
            if d == NORTH:
                minC += 1
            d = (d + 1) % 4
            r, c = dirTable[d](r, c)

    return results


def find_spiral_2(matrix):
    if not matrix or not matrix[0]:
        return []

    minR = 0
    maxR = len(matrix) - 1
    minC = 0
    maxC = len(matrix[0]) - 1
    
    def isValid():
        return minR <= maxR and minC <= maxC
        
    results = []
    r, c = 0, 0
    while isValid():
        # append East
        r, c = minR, minC
        for i in range(maxC - minC + 1):
            results.append(matrix[r][c + i])
        minR += 1
        
        # append South
        if isValid():
            r, c = minR, maxC
            for i in range(maxR - minR + 1):
                results.append(matrix[r + i][c])
        maxC -= 1
        
        # append West
        if isValid():
            r, c = maxR, maxC
            for i in range(maxC - minC + 1):
                results.append(matrix[r][c - i])
        maxR -= 1
        
        # append North
        if isValid():
            r, c = maxR, minC
            for i in range(maxR - minR + 1):
                results.append(matrix[r - i][c])
        minC += 1
        
    return results


def find_spiral_3(matrix):
    results = []
    if not matrix or not matrix[0]:
        return results

    minR, maxR = 0, len(matrix) - 1
    minC, maxC = 0, len(matrix[0]) - 1
        
    while minR <= maxR and minC <= maxC:
        # append East
        for c in range(minC, maxC + 1):
            results.append(matrix[minR][c])
        minR += 1
        
        # append South
        for r in range(minR, maxR + 1):
            results.append(matrix[r][maxC])
        maxC -= 1
        
        # append West
        if minR <= maxR:
            for c in range(maxC,  minC - 1, -1):
                results.append(matrix[maxR][c])
        maxR -= 1
        
        # append North
        if minC <= maxC:
            for r in range(maxR, minR - 1, -1):
                results.append(matrix[r][minC])
        minC += 1
        
    return results

###############################################################################

import unittest

class Test_Matrix_Spiral(unittest.TestCase):

    I = 'input'
    E = 'expected'

    def setUp(self):
        I = self.I
        E = self.E

        self.tests = [
            {
                I: [[1, 2],
                    [3, 4]],
                E: [1, 2, 4, 3]
            },
            {
                I: [[1, 2, 3],
                    [4, 5, 6]],
                E: [1, 2, 3, 6, 5, 4]
            },
            {
                I: [[1, 2],
                    [3, 4],
                    [5, 6]],
                E: [1, 2, 4, 6, 5, 3]
            },
            {
                I: [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                E: [1, 2, 3, 6, 9, 8, 7, 4, 5]
            },
            {
                I: [[ 1,  2,  3,  4,  5,  6],
                    [ 7,  8,  9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18]],
                E: [1, 2, 3, 4, 5, 6, 12, 18, 17,
                    16, 15, 14, 13, 7, 8, 9, 10, 11]
            },
            {
                I: [[ 1,  2,  3],
                    [ 4,  5,  6],
                    [ 7,  8,  9],
                    [10, 11, 12]],
                E: [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
            },
            {
                I: None,
                E: []
            },
            {
                I: [],
                E: []
            },
            {
                I: [[]],
                E: []
            },
        ]

    def test_find_spiral_1(self):
        I = self.I
        E = self.E
        for t in self.tests:
            i = t[I]
            e = t[E]
            self.assertEqual(find_spiral_1(i), e)

    def test_find_spiral_2(self):
        I = self.I
        E = self.E
        for t in self.tests:
            i = t[I]
            e = t[E]
            self.assertEqual(find_spiral_2(i), e)

    def test_find_spiral_3(self):
        I = self.I
        E = self.E
        for t in self.tests:
            i = t[I]
            e = t[E]
            self.assertEqual(find_spiral_3(i), e)

if __name__ == '__main__':
    unittest.main()
