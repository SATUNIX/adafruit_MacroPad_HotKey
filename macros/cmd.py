from adafruit_hid.keycode import Keycode

app = {
    'name': 'CMD',
    'macros': [
        (0x333300, 'WHO', ['whoami\n']),
        (0x333300, 'IPCFG', ['ipconfig\n']),
        (0x333300, 'PING', ['ping 8.8.8.8\n']),
        (0x333300, 'DIR', ['dir\n']),
        (0x333300, 'CLS', ['cls\n']),
        (0x333300, 'CD', ['cd ..\n']),
        (0x333300, 'HOST', ['hostname\n']),
        (0x333300, 'NETST', ['netstat -an\n']),
        (0x333300, 'TASK', ['tasklist\n']),
        (0x333300, 'SHDN', ['shutdown /s /t 0\n']),
        (0x333300, 'EXIT', ['exit\n']),
        (0x333300, 'COLR', ['color 0a\n']),
    ]
}
