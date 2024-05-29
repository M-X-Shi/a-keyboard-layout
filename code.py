# Write your code here :-)
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

L1 = KC.MO(1)
L2 = KC.MO(2)

LCTL_N5 = KC.HT(KC.N5, KC.LCTL, prefer_hold=False)
LGUI_N2 = KC.HT(KC.N2, KC.LGUI, prefer_hold=False)
RCTL_N8 = KC.HT(KC.N8, KC.RCTL, prefer_hold=False)
RGUI_MINS = KC.HT(KC.MINS, KC.RGUI, prefer_hold=False)
LALT_ENT = KC.HT(KC.ENT, KC.LALT, prefer_hold=False)

L2_B = KC.HT(KC.B, L2, prefer_hold=False)

NEQ = send_string('!=')
EQEQ = send_string('==')
PTR = send_string('->')
LTHE = send_string('<=')
GTHE = send_string('>=')
RETN = send_string('return')
ADDE = send_string('+=')
SUBE = send_string('-=')
MULE = send_string('*=')
DIVE = send_string('/=')
MODE = send_string('%=')

keyboard.col_pins = (board.GP1, board.GP2, board.GP5, board.GP7, board.GP9, board.GP14,
                     board.GP28, board.GP22, board.GP21, board.GP20, board.GP19, board.GP17)
keyboard.row_pins = (board.GP0, board.GP12, board.GP13, board.GP15, board.GP18, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.NO

keyboard.keymap = [
    # layer 0
    [_______, _______, KC.LALT, KC.LSFT, KC.GRV,  _______, _______, KC.BSLS, KC.RSFT, KC.RALT, KC.BSPC, _______,
     KC.N1,   LGUI_N2, KC.N3,   KC.N4,   LCTL_N5, KC.N6,   KC.N7,   RCTL_N8, KC.N9,   KC.N0,   RGUI_MINS,KC.EQL,
     KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.ESC,
     KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
     _______, KC.Z,    KC.X,    KC.C,    KC.V,    L2_B,    L2_B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
     _______, _______, _______, L1,      LALT_ENT,_______, _______, KC.SPC,  L1,      _______, _______, _______,],

    # layer 1
    [_______, _______, KC.NO,   KC.NO,   KC.NO,   _______, _______, KC.NO,   KC.NO,   KC.NO,   KC.DEL,  _______,
     KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LCBR, KC.RCBR, KC.PGUP, KC.HOME, KC.UP,   KC.END,  KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LPRN, KC.RPRN, KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, KC.NO,   KC.NO,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.LBRC, KC.RBRC, KC.NO,   KC.NO,   LTHE,    GTHE,    KC.NO,   KC.NO,
     _______, _______, _______, KC.NO,   KC.NO,   _______, _______, KC.NO,   KC.NO,   _______, _______, _______,],

    # layer 2
    [_______, _______, KC.NO,   KC.NO,   KC.NO,   _______, _______, KC.NO,   KC.NO,   KC.NO,   _______, _______,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     _______, _______, _______, KC.NO,   KC.NO,   _______, _______, KC.NO,   _______, _______, _______, _______,],

     # layer 3
    [_______, _______, KC.NO,   KC.NO,   KC.NO,   _______, _______, KC.NO,   KC.NO,   KC.NO,   _______, _______,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     _______, _______, _______, KC.NO,   KC.NO,   _______, _______, KC.NO,   KC.NO,   _______, _______, _______,]
]

if __name__ == '__main__':
    keyboard.go()
