import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.col_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
        self.row_pins = (board.GP27, board.GP5, board.GP26, board.GP6, board.GP15, board.GP7, board.GP14, board.GP8)
        self.diode_orientation = DiodeOrientation.COLUMNS

        self.coord_mapping = [
             0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                         33, 34, 35, 36
        ]