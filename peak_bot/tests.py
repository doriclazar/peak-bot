#!/usr/bin/env python3
import pytest
import sys
import os
from pkg_resources import resource_filename

try:
    from .peak_bot import PeakBot
    from .tongue.output_control import OutputControl
    from .brain.db_memory.database import Database
    from .brain.fs_memory.file_handler import FileHandler
    from .brain.processing.command_finder import CommandFinder
    from .brain.processing.executor import Executor
    from .ears.listener import Listener
    from .ears.input_control import InputControl
    from .antenna.google_transcriber import GoogleTranscriber
    from .antenna.bing_transcriber import BingTranscriber
    from .antenna.peak_connection import PeakConnection

except SystemError:
    from peak_bot import PeakBot
    from tongue.output_control import OutputControl
    from brain.db_memory.database import Database
    from brain.fs_memory.file_handler import FileHandler
    from brain.processing.command_finder import CommandFinder
    from brain.processing.executor import Executor
    from ears.listener import Listener
    from ears.input_control import InputControl
    from antenna.google_transcriber import GoogleTranscriber
    from antenna.bing_transcriber import BingTranscriber
    from antenna.peak_connection import PeakConnection



supported_platforms = ('windows', 'linux')
if sys.platform not in supported_platforms:
    oc.print(oc.PLAT_NOT_SUP, sys.platform) 
    sys.exit()

verbosity = 0
if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        verbosity = sys.argv[1]

default_directories={
'settings_path':resource_filename(__name__, 'peak_data/configuration/settings.json'),
'audio_base_path':resource_filename(__name__, 'peak_data/configuration/audio_base.json'),
'lang_base_path':resource_filename(__name__, 'peak_data/configuration/lang_base.json'),
'library_path':os.path.dirname(resource_filename(__name__, 'peak_data/library/core.json'))+'/',
'audio_wav_path':os.path.join(os.path.expanduser('~'), '.temp_recording.wav'),
'database_path':os.path.join(os.path.expanduser('~'), '.peak_bot.db'),
'modules_path':'modules',
}

test_bot = PeakBot()


def test_oc():
    test_bot.output_control = OutputControl(range(0, 8), str(verbosity), '%')
def test_fh():
    test_bot.file_handler = FileHandler(test_bot.output_control)
def test_ic():
    test_bot.input_control = InputControl(test_bot.output_control)

