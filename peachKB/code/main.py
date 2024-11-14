import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split

keyboard = KMKKeyboard()

keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
split = Split(data_pin=keyboard.data_pin,data_pin2 = keyboard.data_pin2, use_pio=True)
keyboard.modules.append(split)

_______  = KC.TRNS
XXXXXXX  = KC.NO

keyboard.keymap = [
    [ #windows
        KC.ESC,        KC.F1, KC.F2, KC.F3, KC.F4,  KC.F5,           KC.F6, KC.F7, KC.F8,  KC.F9, KC.F10, KC.F11, KC.F12,   KC.PSCR, KC.SLCK, KC.HT(KC.PAUS, KC.TG(1)),

        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,         KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL,   KC.BSPC,   KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,     KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,          KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,KC.LBRC,KC.RBRC, KC.BSLS,   KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS,     KC.A,  KC.S,  KC.D,  KC.F,  KC.G,           KC.H,  KC.J,  KC.K,  KC.L, KC.SCLN, KC.QUOT,     KC.ENT,
        KC.LSFT,      KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,   KC.B,   KC.N,  KC.M, KC.COMM, KC.DOT, KC.SLSH,         KC.RSFT,            KC.UP,
        KC.LCTL, KC.LGUI, KC.LALT,      KC.SPACE,       KC.SPACE,      KC.SPACE,       KC.RALT, KC.RGUI, KC.SEL, KC.RCTL,   KC.LEFT, KC.DOWN, KC.RGHT
    ],
    [ #mac
        KC.ESC,        KC.F1, KC.F2, KC.F3, KC.F4,  KC.F5,           KC.F6, KC.F7, KC.F8,  KC.F9, KC.F10, KC.F11, KC.F12,   KC.PSCR, KC.SLCK, KC.HT(KC.PAUS, KC.TG(2)),

        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,         KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL,   KC.BSPC,   KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,     KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,          KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,KC.LBRC,KC.RBRC, KC.BSLS,   KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS,     KC.A,  KC.S,  KC.D,  KC.F,  KC.G,           KC.H,  KC.J,  KC.K,  KC.L, KC.SCLN, KC.QUOT,     KC.ENT,
        KC.LSFT,      KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,   KC.B,   KC.N,  KC.M, KC.COMM, KC.DOT, KC.SLSH,         KC.RSFT,            KC.UP,
        KC.LCTL, KC.LALT, KC.LGUI,      KC.SPACE,       KC.SPACE,      KC.SPACE,       KC.RALT, KC.RGUI, KC.SEL, KC.RCTL,   KC.LEFT, KC.DOWN, KC.RGHT
    ],
    [ #windows-forMe
        KC.ESC,        KC.F1, KC.F2, KC.F3, KC.F4,  KC.F5,           KC.F6, KC.F7, KC.F8,  KC.F9, KC.F10, KC.F11, KC.F12,   KC.PSCR, KC.SLCK, KC.HT(KC.PAUS, KC.TG(0)),

        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,         KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL,   KC.BSPC,   KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,     KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,          KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,KC.LBRC,KC.RBRC, KC.BSLS,   KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS,     KC.A,  KC.S,  KC.D,  KC.F,  KC.G,           KC.H,  KC.J,  KC.K,  KC.L, KC.SCLN, KC.QUOT,     KC.ENT,
        KC.LSFT,      KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,   KC.B,   KC.N,  KC.M, KC.COMM, KC.DOT, KC.SLSH,         KC.RSFT,            KC.UP,
        KC.LGUI, KC.LALT, KC.LCTL,      KC.SPACE,       KC.SPACE,      KC.SPACE,       KC.RALT, KC.RGUI, KC.SEL, KC.RCTL,   KC.LEFT, KC.DOWN, KC.RGHT
    ],
]

if __name__ == '__main__':
    keyboard.go()
