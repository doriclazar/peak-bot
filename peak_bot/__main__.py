#!/usr/bin/env python3
import sys, os, re, argparse
from pkg_resources import resource_filename

try:
    from .peak_bot import PeakBot
except SystemError:
    from peak_bot import PeakBot


default_directories={
'settings_path':    resource_filename(__name__, 'peak_data/configuration/settings.json'),
'audio_base_path':  resource_filename(__name__, 'peak_data/configuration/audio_base.json'),
'lang_base_path':   resource_filename(__name__, 'peak_data/configuration/lang_base.json'),
'library_path':     os.path.dirname(resource_filename(__name__, 'peak_data/library/core.json'))+'/',
'audio_wav_path':   os.path.join(os.path.expanduser('~'), '.temp_recording.wav'),
'database_path':    os.path.join(os.path.expanduser('~'), '.peak_bot.db'),
'modules_path':     'modules',
}


def main():
    supported_platforms = ('windows', 'linux')
    if sys.platform not in supported_platforms:
        oc.print(oc.PLAT_NOT_SUP, sys.platform) 
        sys.exit()

    directories = default_directories

    parser=argparse.ArgumentParser()
    parser.add_argument('-s','--settings',  help='Settings file path. Defaults to "peak_data/configuration/settings.json".')
    parser.add_argument('-l','--language',  help='Language file path. Defaults to "peak_data/configuration/lang_base.json".')
    parser.add_argument('-L','--library',   help='Library file path. Defaults to "peak_data/library/core.json".')
    parser.add_argument('-w','--wave',      help='Wave file path. Defaults to ".temp_recording.wav".')
    parser.add_argument('-a','--audio',     help='Audio file path. Defaults to "peak_data/configuration/audio_base.json".')
    parser.add_argument('-d','--data',      help='Database file path. Defaults to ".peak_bot.db".')
    parser.add_argument('-P','--peak',      help='Peak hostname. Accepts IP address, or hostname.')
    parser.add_argument('-v','--verbose',   help='Print more info during run.', action='store_true')

    # activate after handling in peak_bot.py *2
    #parser.add_argument('-T','--transcriber',help='Transcriber type. Defalts to "google_transcriber"')
    #parser.add_argument('-t','--translator',help='Translator type. Defalts to "google_translator"')
    args=parser.parse_args()

    verbose = False
    if args.verbose:
        verbose = True

    if args.data: 
        if os.path.isfile(os.path.dirname(args.data)):
            directories['database_path'] = args.data
        elif verbose:
            #fix output *1
            print('NO SUCH DIRECTORY')

    if args.library: 
        if os.path.isfile(args.library):
            directories['library_path'] = args.library
        elif verbose:
            #fix output *1
            print('NO SUCH FILE')

    if args.language: 
        if os.path.isfile(args.language):
            directories['lang_base_path'] = args.language
        elif verbose:
            #fix output *1
            print('NO SUCH FILE')

    if args.wave: 
        if os.path.isfile(os.path.dirname(args.wave)):
            directories['audio_wav_path'] = args.wave
        elif verbose:
            #fix output *1
            print('NO SUCH DIRECTORY')

    if args.audio: 
        if os.path.isfile(args.audio):
            directories['audio_base_path'] = args.audio
        elif verbose:
            #fix output *1
            print('NO SUCH FILE')

    pk_server=None
    if args.peak: 
        ip_reg = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
        hostname_reg = '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'
        if re.match(ip_reg, args.peak) or re.match(hostname_reg, args.peak):
            pk_server = args.peak
        elif verbose:
            #fix output *1
            print('BAD INPUT')

    # Remove, and returtn to using __init__(..., trans=None) for PeakBot
    ts_translator=None
    st_transcriber=None

    bot = PeakBot(default_directories, verbose, pk_server, st_transcriber, ts_translator)
    bot.run_bot()
    bot.database.connection.close()
    bot.output_control.print(bot.output_control.DB_CON_CLOSED)
        
if __name__ == '__main__':
    main()

# TESTING:
from io import StringIO
from contextlib import contextmanager

class TestBot(object):
    @contextmanager
    def force_input(self, input_text):
        initial = sys.stdin
        sys.stdin = input_text 
        yield
        sys.stdin = initial

    test_bot = PeakBot(default_directories, False)

    def test_models_integrity(self):
        tables = [('languages',),('sqlite_sequence',),('modules',),('external_modules',),
                ('commands',),('imports',),('calls',),('words',),('combos',)]
        assert tables == list(self.test_bot.database.cursor.execute('select name from sqlite_master where type = "table"'))

    def test_oc(self):
        assert self.test_bot.output_control is not None


    # Expand to work with multi-layered commands (eg. copy ... which file? ... test.txt).
    def test_bot_run(self):
        with self.force_input(StringIO("exit now")):
            self.test_bot.run_bot()
        self.test_bot.database.connection.close()

