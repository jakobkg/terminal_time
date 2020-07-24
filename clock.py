from typing import TypeVar
from argparse import ArgumentParser
from datetime import datetime, timedelta
import re, os, threading

parser = ArgumentParser(description='What time is it? I\'m near-sighted.')
parser.add_argument('-l', '--loop',
                    help='The clock "takes over" the terminal it\'s in, instead of printing the current time and exiting', 
                    action='store_true')

parser.add_argument('-s', '--seconds',
                    help='Show seconds. By default time is shown as HH:MM, adding this flag changes format to HH:MM:SS',
                    action='store_true')

parser.add_argument('-f', '--filename',
                    help='File to load the font from. Default uses the bundled font file')

Number = TypeVar('Number', int, float, complex)


def get_digit(number: Number, n: Number) -> int:
    return number // 10**n % 10


def clock(loop: bool, showSeconds: bool) -> None:
    currentTime = datetime.now().time()
    hours = currentTime.hour
    minutes = currentTime.minute
    seconds = currentTime.second

    global prevTime

    if showSeconds or minutes != prevTime.minute:
        prevTime = currentTime

        printbuf = ''
        if loop:
            os.system('cls' if os.name == 'nt' else 'clear')

        for offset in range(fontSize):
            printbuf += fontbuf[fontSize * get_digit(hours, 1) + offset] + fontbuf[fontSize * get_digit(hours, 0) + offset]
            printbuf += fontbuf[10 * fontSize + offset]
            printbuf += fontbuf[fontSize * get_digit(minutes, 1) + offset] + fontbuf[fontSize * get_digit(minutes, 0) + offset]
            if showSeconds:
                printbuf += fontbuf[10 * fontSize + offset]
                printbuf += fontbuf[fontSize * get_digit(seconds, 1) + offset] + fontbuf[fontSize * get_digit(seconds, 0) + offset]
            printbuf += '\n'

        print(printbuf, end='')
    if loop:
        threading.Timer(1 if showSeconds else 10, clock, args=(loop, showSeconds)).start()


args = parser.parse_args()

fontFilename = args.filename if args.filename else 'font'
fontPath = os.path.dirname(__file__) + '/' + fontFilename

printbuf = ''

prevTime = datetime.today() - timedelta(minutes=1)

with open(fontPath, 'r') as f:
    fontbuf = re.split('\n', f.read())

fontSize = len(fontbuf) // 11

clock(args.loop, args.seconds)
