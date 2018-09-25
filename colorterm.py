import sys

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())

cprint(figlet_format('I eat ass', font='big'),
        'yellow', 'on_red', attrs = ['bold'])
