from adafruit_hid.keycode import Keycode

app = {
    'name': 'ADMIN',
    'macros': [
        (0x0013ff, 'SUDO', ['sudo su\n']),
        (0x0013ff, 'ROOT', ['sudo -i\n']),
        (0x0013ff, 'USR', ['whoami\n']),
        (0x0013ff, 'HOST', ['hostname\n']),
        (0x0013ff, 'IPa', ['ip a\n']),
        (0x0013ff, 'IPr', ['ip r\n']),
        (0x0013ff, 'DNS', ['cat /etc/resolv.conf\n']),
        (0x0013ff, 'EDIT', ['nano /etc/hosts\n']),
        (0x0013ff, 'TIME', ['date\n']),
        (0x0013ff, 'PS', ['ps aux\n']),
        (0x0013ff, 'SVC', ['systemctl status\n']),
        (0x0013ff, 'UPDT', ['sudo apt update && sudo apt upgrade\n']),
    ]
}

