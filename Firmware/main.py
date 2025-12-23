import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# ─────────────────────────
# Keys
# order is important!
# SW1, SW2, SW3, SW4, SW5, SW6
PINS = [
    board.D1,  # SW1
    board.D2,  # SW2
    board.D3,  # SW3
    board.D4,  # SW4
    board.D7,  # SW5
    board.D8,  # SW6
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ─────────────────────────
# key binds
keyboard.keymap = [
    [
        KC.MUTE,                    # SW1
        KC.PGUP,                    # SW2
        KC.LWIN(KC.LEFT),           # SW3
        KC.LWIN(KC.RIGHT),          # SW4
        KC.PGDN,                    # SW5
        KC.ENTER,                   # SW6
    ]
]

# ─────────────────────────
# ROTARY ENCODER (SW10)
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D5, board.D6),  # A, B пины энкодера
)

encoder.map = [
    (
        KC.VOLU,  # clockwise
        KC.VOLD,  # anticlockwise
    )
]

# ─────────────────────────
if __name__ == '__main__':
    keyboard.go()
