#!/usr/bin/env python3
import os
import sys

from pkg_resources import resource_filename
from .peak_bot import PeakBot

def main():
    supported_platforms = ('windows', 'linux')
    if sys.platform not in supported_platforms:
        oc.print(oc.PLAT_NOT_SUP, sys.platform) 
        sys.exit()

    verbosity = 0
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            verbosity = sys.argv[1]

    settings_path = resource_filename(__name__, "peak_data/configuration/settings.json")
    audio_base_path = resource_filename(__name__, "peak_data/configuration/audio_base.json")
    lang_base_path = resource_filename(__name__, "peak_data/configuration/lang_base.json")
    library_path = os.path.dirname(resource_filename(__name__, "peak_data/library/core.json"))+ '/'
    audio_wav_path = os.path.join(os.path.expanduser("~"), ".temp_recording.wav")
    database_path = os.path.join(os.path.expanduser("~"), ".peak_bot.db")
    modules_path = "modules"
    fundamental_directories = (settings_path, audio_base_path, lang_base_path, library_path, audio_wav_path, database_path, modules_path)
    bot = PeakBot(fundamental_directories, verbosity)
        
if __name__ == '__main__':
    main()
