from adafruit_hid.keycode import Keycode

app = {
    'name': 'HACK 0',
    'macros': [
        (0xFF0000, 'HTB', ['https://www.hackthebox.com\n']),
        (0xFF0000, 'THM', ['https://tryhackme.com\n']),
        (0xFF0000, 'MITRE', ['https://attack.mitre.org\n']),
        (0xFF0000, 'CVE', ['https://cve.mitre.org\n']),
        (0xFF0000, 'ExDB', ['https://exploit-db.com\n']),
        (0xFF0000, 'VRSTTL', ['https://www.virustotal.com\n']),
        (0xFF0000, 'PAYLOAD', ['https://github.com/swisskyrepo/PayloadsAllTheThings\n']),
        (0xFF0000, 'OWASP', ['https://owasp.org/www-project-top-ten/\n']),
        (0xFF0000, 'HEADER', ['https://securityheaders.com\n']),
        (0xFF0000, 'SHODAN', ['https://www.shodan.io\n']),
        (0xFF0000, 'NETSEC', ['https://reddit.com/r/netsec\n']),
    ]
}
