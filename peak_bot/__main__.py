#!/usr/bin/env python3
import os
import sys

'''
Display options: 
    Qt      - peak_ui: "https://github.com/doriclazar/peak_ui"
    Tkinter - in queue.
    Cli     - default, this.
'''


'''
Clone
'''
from peak_bot import PeakBot
'''
PyPI deploy
from pkg_resources import resource_filename
from .peak_bot import PeakBot
'''

def main():
    supported_platforms = ('windows', 'linux')
    if sys.platform not in supported_platforms:
        oc.print(oc.PLAT_NOT_SUP, sys.platform) 
        sys.exit()

    verbosity = 0
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            verbosity = sys.argv[1]

    '''
    Clone
    '''
    default_directories={
    'settings_path':'peak_data/configuration/settings.json',
    'audio_base_path':'peak_data/configuration/audio_base.json',
    'lang_base_path':'peak_data/configuration/lang_base.json',
    'library_path':'peak_data/library/',
    'audio_wav_path':'brain/fs_memory/.temp_recording.wav',
    'database_path':'peak_bot.db',
    'modules_path':'modules',
    }

    '''
    PyPI deploy
    default_directories={
    'settings_path':resource_filename(__name__, 'peak_data/configuration/settings.json'),
    'audio_base_path':resource_filename(__name__, 'peak_data/configuration/audio_base.json'),
    'lang_base_path':resource_filename(__name__, 'peak_data/configuration/lang_base.json'),
    'library_path':os.path.dirname(resource_filename(__name__, 'peak_data/library/core.json'))+'/',
    'audio_wav_path':os.path.join(os.path.expanduser('~'), '.temp_recording.wav'),
    'database_path':os.path.join(os.path.expanduser('~'), '.peak_bot.db'),
    'modules_path':'modules',
    }
    '''
    bot = PeakBot(default_directories, verbosity)
    bot.run_bot()
    bot.database.connection.close()
    bot.output_control.print(bot.output_control.DB_CON_CLOSED)
        
if __name__ == '__main__':
    main()
