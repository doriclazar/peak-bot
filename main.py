#!/usr/bin/env python3
import os
import sys

from tongue.output_control import OutputControl
from peak_bot import PeakBot

def main():
    '''
    Sets the verbosity in respect to the user input.
    Checks if settings are good.
    Instantiate a peak-bot.
     '''
    verbosity = 0
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            verbosity = sys.argv[1]

    oc = OutputControl(range(0, 8), str(verbosity))
    oc.print(oc.WELCOME_MSG) 
    if os.path.exists('configuration/settings.json'):
        oc.print(oc.SPLITTER)
        bot = PeakBot('configuration/settings.json', oc)
    else:
        oc.print(oc.SETT_FILE_NOT_FOUND, ('configuration/settings.json',))
        sys.exit()

main()
