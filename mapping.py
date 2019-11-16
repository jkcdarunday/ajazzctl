commands = {
    'start': [1],
    'end': [2],
    'read_mem': [5, 56],  # (unconfirmed) looks like followed by byte index
    'set_mode': [6, 1],
    'reverse_wave': [6, 1, 4],  # data is 1 for left to right (wave) or outwards (wave_centered) otherwise, 0
    'set_key_color': [17, 3],  # followed by key value
    'set_brightness': [6, 1, 1],  # data is 0x00 - 0x19 for brightness
    'set_speed': [6, 1, 2],  # data is 0x00 - 0x19 for speed (19 is slowest
    'set_global_color': [6, 3, 5],  # data is r g b
    'set_random_color': [6, 1, 8],  # 1 or 0
    'set_drop_size': [6, 1, 15]  # 1 or 0
}

# Commands used during reset:
# - [0x6, 0x23] data : [1, 0x14, 5, [0, 0, 0xff, 0xff, 0xff] *  6]
# - Set mode to wave
# - Continuous call [0x11, 0x36, (0x0 to 0xb0 0x01 stepped by 0x36)] data: [0xff] * 54
#   - third vals: 0x00, 0x36, 0x6c, 0xa2, 0xd8, [0x0e, 0x01], [0x7a, 0x01], [0x44, 0x01], [0x7a, 0x01], [0xb0, 0x01]
# - [0x0a 0x10] data: [0xaa 0x55 0x10 0 0 0 1 0 2]
#   - ^ immediately followed by [0x08 0x38] data: [5, 0, 0] * 6 + [0] * 6 + [2 2 0x29 2 2 0x35 22 0x2b 22 0x39 2 1 2 2] [1 1 0*5] [2 2 3a 2 2 1e 2 2] (What the heck is this)
#   - ^ happens 8 times with different data. This looks like firmware update?
#   - ends with [0x8 0x20] and some weird data again
#   - closes but follows with [0x03, 0x20]
# - finally ends with [0x05, 0x38]


modes = {
    'wave': [1],
    'off': [2],
    'spectrum': [3],
    'drop': [4],
    'static': [5],
    'zoom': [9],
    'breathe': [11],
    'ripple': [12],
    'rain': [16],
    'wave_centered': [17],
    'tornado': [18]
}

keys = {
    'esc': [0x18],
    'f1': [0x30],
    'f2': [0x48],
    'f3': [0x60],
    'f4': [0x78],
    'f5': [0x90],
    'f6': [0xa8],
    'f7': [0xc0],
    'f8': [0xd8],
    'f9': [0xf0],
    'f10': [0x08, 0x01],  # 01
    'f11': [0x20, 0x01],  # 01
    'f12': [0x38, 0x01],  # 01
    'prtsc': [0x72],
    'scrlk': [0x8a],
    'pause': [0xba],

    # line2
    '`': [0x1b],
    '1': [0x33],
    '2': [0x4b],
    '3': [0x63],
    '4': [0x7b],
    '5': [0x93],
    '6': [0xab],
    '7': [0xc3],
    '8': [0xdb],
    '9': [0xf3],
    '0': [0x0b, 1],
    '-': [0x23, 1],
    '=': [0x3b, 1],
    'backspace': [0x47, 1],

    'insert': [0xd2],
    'home': [0xea],
    'pgup': [0x2, 1],

    'numlock': [0x53, 1],
    'num/': [0x6b, 1],
    'num*': [0x83, 1],
    'num-': [0x62, 1],

    # line3
    'tab': [0x1e],
    'q': [0x36],
    'w': [0x4e],
    'e': [0x66],
    'r': [0x7e],
    't': [0x96],
    'y': [0xae],
    'u': [0xc6],
    'i': [0xde],
    'o': [0xf6],
    'p': [0x0e, 1],
    '[': [0x26, 1],
    ']': [0x3e, 1],
    '\\': [0x41, 1],

    'del': [0x1a, 1],
    'end': [0x32, 1],
    'pgdn': [0x4a, 1],

    'num7': [0x56, 1],
    'num8': [0x6e, 1],
    'num9': [0x86, 1],
    'num+': [0x7a, 1],

    # line4
    'caps': [0x21],
    'a': [0x39],
    's': [0x51],
    'd': [0x69],
    'f': [0x81],
    'g': [0x99],
    'h': [0xb1],
    'j': [0xc9],
    'k': [0xe1],
    'l': [0xf9],
    ';': [0x11, 1],
    '\'': [0x29, 1],
    'enter': [0x44, 1],

    'num4': [0x59, 1],
    'num5': [0x71, 1],
    'num6': [0x89, 1],

    # line5
    'lshift': [0x24],
    'z': [0x3c],
    'x': [0x54],
    'c': [0x6c],
    'v': [0x84],
    'b': [0x9c],
    'n': [0xb4],
    'm': [0xcc],
    ',': [0xe4],
    '.': [0xfc],
    '/': [0x14, 1],
    'rshift': [0x2c, 1],

    'up': [0x17, 1],

    'num1': [0x5c, 1],
    'num2': [0x74, 1],
    'num3': [0x8c, 1],

    'numenter': [0x8f, 1],

    # line6
    'lctrl': [0x27],
    'lwin': [0x3f],
    'lalt': [0x57],
    'space': [0x6f],
    'ralt': [0x87],
    'fn': [0x9f],
    'menu': [0xb7],
    'rctrl': [0xcf],
    'left': [0xe7],
    'down': [0xff],
    'right': [0x2f, 1],
    'num0': [0x5f, 1],

    'num.': [0x77, 1],
}
