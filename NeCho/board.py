class Board:

    # Initialize the board
    def __init__(self, colour):
        self.colour = colour
        self.board = \
            [[Spot("black", 1) if ((y == 6 or y == 7) and (x != 2 and x != 5))
              else Spot("white", 1) if ((y == 0 or y == 1) and (x != 2 and x != 5))
              else None for y in range(8)] for x in range(8)]
        self.black = [(0, 7), (1, 7), (3, 7), (4, 7), (6, 7), (7, 7), (0, 6), (1, 6), (3, 6), (4, 6), (6, 6), (7, 6)]
        self.white = [(0, 1), (1, 1), (3, 1), (4, 1), (6, 1), (7, 1), (0, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0)]

    def print_board(self):
        template = """# {}
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,7 | 1,7 | 2,7 | 3,7 | 4,7 | 5,7 | 6,7 | 7,7 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,6 | 1,6 | 2,6 | 3,6 | 4,6 | 5,6 | 6,6 | 7,6 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 | 7,4 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 | 7,3 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 | 7,2 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 | 7,1 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+
        # | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
        # | 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 | 7,0 |
        # +-----+-----+-----+-----+-----+-----+-----+-----+"""

        coords = [(x, 7 - y) for y in range(8) for x in range(8)]
        cells = []
        for (x, y) in coords:
            spot = self.board[x][y]
            cells.append(("" if not spot else str(spot.colour)[0].upper() + str(spot.n)).center(3))

        print(template.format("Board", *cells))
        print("remaining black positions: ", self.black)
        print("remaining white positions: ", self.white)


class Spot:

    def __init__(self, colour, n):
        self.colour = colour
        self.n = n
        self.targets = []

    pass
