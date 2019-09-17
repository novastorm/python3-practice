class GameOfLife:
    def __init__(self, board):
        self._board = board

    def __iter__(self):
        return self

    def __next__(self):
        neighbors = {}
        oldBoard = self._board.copy()
        newBoard = set()

        for pos in self._board:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 == dx == dy:
                        continue
                    neighbor = (pos[0] + dx, pos[1] + dy)
                    neighbors[neighbor] = neighbors.get(neighbor, 0) + 1

        for (pos, value) in neighbors.items():
            if value == 3 or (value == 2 and (pos in self._board)):
                newBoard.add(pos)

        self._board.clear()
        self._board |= newBoard

        return oldBoard


from curses import wrapper, curs_set

flasher = set([(1,0), (1,1), (1,2)])
glider = set([
    (0,1),
    (1,2),
    (2,0),
    (2,1),
    (2,2)
    ])

def main(stdscr, board):
    gol = GameOfLife(board)
    it = iter(gol)

    curs_set(0)

    for i in range(10):
        stdscr.clear()
        snapshot = next(it)

        for r in range(10):
            for c in range(10):
                if (r,c) in snapshot:
                    stdscr.addstr(r, c, "*")
                # else:
                #     stdscr.addstr(" ")

        stdscr.refresh()
        stdscr.getkey()

    curs_set(1)

if __name__ == '__main__':
    wrapper(main, flasher)
    wrapper(main, glider)
