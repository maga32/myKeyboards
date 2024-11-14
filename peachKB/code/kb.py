import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):

    col_pins = (board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP26)
    row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
    data_pin = board.GP29
    data_pin2 = None
    diode_orientation  = DiodeOrientation.COL2ROW

    coord_mapping  = [
         7,     6,  5,  4,  3,    2,         69, 68, 67,  66, 65, 64, 63,   62, 61, 60,

        27, 17, 16, 15, 14, 13, 12,         79, 78, 77, 76, 75, 74,   73,   72, 71, 70,
        37,   26, 25, 24, 23, 22,         99, 89, 88, 87, 86, 85, 84, 83,   82, 81, 80,
        47,   36, 35, 34, 33, 32,         109, 98, 97, 96, 95, 94,    93,
        57,    46, 45, 44, 43, 42,   119,   108,107,106,105,104,     103,      101,
        56,  55,  54,    53,          118,    117,  116, 117,  114,  113,  112,111,110
    ]
