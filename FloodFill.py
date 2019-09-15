import json

class Canvas:
    def __init__(self, buffer, height, width):
        self._buffer = buffer
        self._height = height
        self._width = width


    @property
    def height(self):
        return self._height
    

    @property
    def width(self):
        return self._width


    @property
    def buffer(self):
        return self._buffer


    def __str__(self):
        return json.dumps(self._buffer)
    

    def getColorAtPosition(self, pos):
        row, col = pos
        i = self._width * row + col
        return self._buffer[i]


    def setColorAtPosition(self, pos, color):
        row, col = pos
        i = self._width * row + col
        self._buffer[i] = color
    

def floodFill(canvas, pos, color):
    pending = [pos]
    oldColor = canvas.getColorAtPosition(pos)
    canvas.setColorAtPosition(pos, color)

    while pending:
        curr = pending.pop(0)

        for newPos in getNeighbors(canvas, curr, oldColor):
            canvas.setColorAtPosition(newPos, color)
            pending.append(newPos)


def getNeighbors(canvas, pos, color):
    results = []

    # r, c = pos
    # # North
    # if 0 <= r - 1 and canvas.getColorAtPosition((r - 1, c)) == color:
    #     results.append((r - 1, c))
    # # South
    # if r + 1 < canvas.height and canvas.getColorAtPosition((r + 1, c)) == color:
    #     results.append((r + 1, c))
    # # West
    # if 0 <= c - 1 and canvas.getColorAtPosition((r, c - 1)) == color:
    #     results.append((r, c - 1))
    # # East
    # if c + 1 < canvas.width and canvas.getColorAtPosition((r, c + 1)) == color:
    #     results.append((r, c + 1))

    kNorth = (-1, 0)
    kSouth = (1, 0)
    kEast  = (0, 1)
    kWest  = (0, -1)

    for dr, dc in (kNorth, kSouth, kEast, kWest):
        r, c = pos
        r += dr
        c += dc
        if (0 <= r < canvas.height 
            and 0 <= c < canvas.width
            and canvas.getColorAtPosition((r, c)) == color):
            results.append((r, c))

    return results


import unittest

class Test_FloodFill(unittest.TestCase):

    def setUp(self):
        width = 5
        height = 4
        image = [
            0, 1, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 1, 0,
            1, 0, 1, 0, 1
        ]

        self.canvas = Canvas(image, height, width)

    def test_1(self):
        floodFill(self.canvas, (1,1), 2)
        expected = [0, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 0, 1, 0, 1]
        self.assertEqual(self.canvas.buffer, expected)


if __name__ == '__main__':
    unittest.main()
