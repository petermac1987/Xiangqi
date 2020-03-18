# Default Program

class XiangqiGame:

    def __init__(self):
        self._game_state = 'UNFINISHED'

        self._the_board = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',
                           'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i2',
                           'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'i3',
                           'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'i4',
                           'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'i5',
                           'a6', 'b6', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',
                           'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',
                           'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',
                           'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',
                           'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1',]

        self._pieces = []

    def get_game_state(self):
        return self._game_state

    def set_active(self, piece, location):
        if location in self._the_board:
            piece.set_location(location)
            self._pieces.append(piece)
            return True
        else:
            return False

class Pieces:

    def __init__(self):
        self._location = None

    # Get methods
    def get_location(self):
        return self._location

    # Set methods
    def set_location(self, coordinate):
        self._location = coordinate

class General(Pieces):

    def __init__(self, player):
        super().__init__()
        self._in_check = False

    def get_in_check(self):
        return self._in_check


class Advisor(Pieces):

    def __init__(self, player):
        super().__init__()


class Elephant(Pieces):

    def __init__(self, player):
        super().__init__()


class Horse(Pieces):

    def __init__(self, player):
        super().__init__()


class Chariot(Pieces):

    def __init__(self, player):
        super().__init__()


class Cannon(Pieces):

    def __init__(self, player):
        super().__init__()


class Soldier(Pieces):

    def __init__(self, player):
        super().__init__()