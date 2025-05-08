from adafruit_hid.keycode import Keycode

app = {
    'name': 'POWERSHELL',
    'macros': [
        (0x112233, 'GETP', ['Get-Process\n']),
        (0x112233, 'GETS', ['Get-Service\n']),
        (0x112233, 'STRTP', ['Start-Process notepad\n']),
        (0x112233, 'STOPS', ['Stop-Service wuauserv\n']),
        (0x112233, 'IP', ['Get-NetIPAddress\n']),
        (0x112233, 'EXEC', ['Set-ExecutionPolicy Unrestricted\n']),
        (0x112233, 'HELP', ['Get-Help Get-Process\n']),
        (0x112233, 'CHLD', ['Get-ChildItem\n']),
        (0x112233, 'WEB', ['Invoke-WebRequest https://osakabbs.com\n']),
        (0x112233, 'CLR', ['Clear-Host\n']),
        (0x112233, 'EXIT', ['exit\n']),
        (0x112233, 'RST', ['Restart-Computer\n']),
    ]
}
