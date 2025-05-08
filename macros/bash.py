from adafruit_hid.keycode import Keycode

app = {
    'name': 'BASH',
    'macros': [
        (0x003300, 'LS', ['ls -lha\n']),
        (0x003300, 'PWD', ['pwd\n']),
        (0x003300, 'BACK', ['cd ..\n']),
        (0x003300, 'VIM', ['vim \n']),
        (0x003300, 'XCTBL', ['chmod +x script.sh\n']),
        (0x003300, 'APT', ['sudo apt update\n']),
        (0x003300, 'SYSLOG', ['tail -f /var/log/syslog\n']),
        (0x003300, 'PING', ['ping 8.8.8.8\n']),
        (0x003300, 'TOP', ['htop\n']),
        (0x003300, 'JOURNAL', ['journalctl -xe\n']),
        (0x003300, 'WHO?', ['whoami\n']),
        (0x003300, 'EXIT', ['exit\n']),
    ]
}
