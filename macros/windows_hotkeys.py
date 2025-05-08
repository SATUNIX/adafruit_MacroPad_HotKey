from adafruit_hid.keycode import Keycode

app = {
    'name': 'Windows',
    'macros': [
        (0x002255, 'DESKT', [Keycode.GUI, Keycode.D]),
        (0x002255, 'RUN', [Keycode.GUI, Keycode.R]),
        (0x002255, 'FILES', [Keycode.GUI, Keycode.E]),
        (0x002255, 'SEARCH', [Keycode.GUI, Keycode.S]),
        (0x002255, 'LOCK', [Keycode.GUI, Keycode.L]),
        (0x002255, 'T_MGR', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]),
        (0x002255, 'OPT', [Keycode.GUI, Keycode.I]),
        (0x002255, 'SSC', [Keycode.GUI, Keycode.SHIFT, Keycode.S]),
        (0x002255, 'MIN', [Keycode.GUI, Keycode.M]),
        (0x002255, 'ATAB', [Keycode.ALT, Keycode.TAB]),
        (0x002255, 'EXIT', [Keycode.ALT, Keycode.F4]),
        (0x002255, 'RESET', [Keycode.CONTROL, Keycode.SHIFT, Keycode.R]),
    ]
}
