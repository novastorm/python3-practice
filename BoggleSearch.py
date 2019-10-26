def boggle_search(board, word):
    maxRows = len(board)
    maxCols = len(board[0])
    for r in range(maxRows):
        for c in range(maxCols):
            results = search(r, c, board, word, "")
            if results:
                return True
    return False


def search(r, c, board, word, predecessor):
    maxRows = len(board)
    maxCols = len(board[0])

    if (r < 0 or r >= maxRows or
        c < 0 or c >= maxCols or
        predecessor not in word or
        board[r][c] == '-'):
        return False

    ch = board[r][c]
    s = predecessor + ch

    results = False

    if s == word:
        return True

    board[r][c] = '-'
    results = (
        search(r - 1, c, board, word, s) or
        search(r + 1, c, board, word, s) or
        search(r, c - 1, board, word, s) or
        search(r, c + 1, board, word, s))
    board[r][c] = ch

    return results


###############################################################################

import unittest


class Test_boggle_search(unittest.TestCase):

    def test_boggle_search(self):
        b = [
            ["A", "O", "L"],
            ["D", "E", "L"],
            ["G", "H", "I"],
        ]
        w = "HELLO"
        e = True
        self.assertEqual(boggle_search(b, w), e)


if __name__ == '__main__':
    unittest.main()
