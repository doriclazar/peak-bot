#!/usr/bin/env python3
import os
import sys

from brain.db_memory.database import Database
from brain.fs_memory.file_handler import FileHandler
from brain.processing.command_finder import CommandFinder
from brain.processing.executor import Executor
from ears.listener import Listener
from ears.input_control import InputControl
from antenna.google_transcriber import GoogleTranscriber
from antenna.bing_transcriber import BingTranscriber

class PeakBot:
    module_dicts = []
    command_list = []
    database_path = ""
    def set_database_path(self):
        '''
        Function for extracting a database path.
        Assumes only one database is active.
        '''
        oc = self.output_control
        oc.print(oc.DB_PATH_SET_ATT)
        try:
            if 'databases' in self.settings_dict:
                for database_data in self.settings_dict['databases']:
                    if database_data['database_active'] == 'True':
                        if database_data['database_engine'] == 'sqlite3':
                            self.database_path = ('{0}{1}'.format(database_data['database_dir'], database_data['database_filename']))
                            oc.print(oc.USING_DB, (database_data['database_filename'],))
                            break
                        elif database_data['database_engine'] in ('MS SQL Server', 'MySql', 'MySql/MariaDB', 'MongoDB'):
                            oc.print(oc.ENGINE_NOT_SUP, (database_data['database_engine'],))
                        else:
                            oc.print(oc.UNKNOWN_ENGINE, (database_data['database_engine'],))
                    else:
                        oc.print(oc.INACTIVE_DB, (database_data['database_filename']),)
                oc.print(oc.DB_PATH_SET)
        except Exception as e:
            oc.print(oc.DB_PATH_NOT_SET, (str(e),))

    def set_modules_and_commands(self):
        '''
        This function is looking for modules and commands in the defined directory.
        'get_modules_and_commands' is using 'FileHandler' class, and it's 'check_path' function.
        '''
        oc = self.output_control
        oc.print(oc.MOD_COM_SET_ATT)
        (self.module_dicts, self.directories) = self.file_handler.check_path(self.settings_dict['library_dir']) 
        try:
            for directory in self.directories:
                if ('{0}.json'.format(directory)) in os.listdir(self.settings_dict['library_dir']):
                    oc.print(oc.JSON_EXISTS, (directory, self.settings_dict['library_dir'], directory))
                    (command_dict, self.skip_directories) = self.file_handler.check_path('{0}{1}/'.format(self.settings_dict['library_dir'], directory))
                    self.command_list.append(command_dict)
                    oc.print(oc.DIR_WITH_COMS, (directory,))
                    oc.print(oc.SKIP_DIRS, (self.skip_directories,))
                else:
                    self.skip_directories.append(directory)
                    self.directories.remove(directory)
                    oc.print(oc.NO_JSON_FILE, (directory,))
            oc.print(oc.MOD_COM_SET)
        except Exception as e:
            oc.print(oc.MOD_COM_NOT_SET, (str(e),))
                
    def init_database(self):
        '''
        Initiates a new database.
        '''
        self.output_control.print(self.output_control.INIT_ATT, ('database',))
        try:
            self.database = Database(self.output_control, self.database_path, self.languages_dict, self.module_dicts, self.command_list)
            self.output_control.print(self.output_control.INIT, ('Database',))
        except Exception as e:
            self.output_control.print(self.output_control.NOT_INIT, ('Database', str(e)))

    def init_listener(self):
        '''
        Initiates a new listener.
        '''
        self.output_control.print(self.output_control.INIT_ATT, ('listener',))
        try:
            self.listener = Listener(self.output_control, self.audio_settings_dict)
            self.output_control.print(self.output_control.INIT, ('Listener',))
        except Exception as e:
            self.output_control.print(self.output_control.NOT_INIT, ('Listener', str(e)))
            sys.exit()

    def init_command_finder(self):
        '''
        Initiates a new command_finder.
        '''
        self.output_control.print(self.output_control.INIT_ATT, ('command finder',))
        try:
            self.command_finder = CommandFinder(self.output_control, self.input_control, self.database)
            self.output_control.print(self.output_control.INIT, ('Command finder',))
        except Exception as e:
            self.output_control.print(self.output_control.NOT_INIT, ('Command finder', str(e)))
            sys.exit()

    def init_transcriber(self, expected_calls):
        '''
        Initiates a new transcriber.

        '''
        speech_apis_dict = {
                'GOOGL': GoogleTranscriber,
                'BING': BingTranscriber
                }
        self.output_control.print(self.output_control.INIT_ATT, ('transcriber',))
        try:
            for speech_api in self.settings_dict['speech_apis']:
                if speech_api['active']:
                    transcriber_type = speech_apis_dict[speech_api['code']]
                    break
            
            self.transcriber = transcriber_type(self.output_control, self.audio_settings_dict, expected_calls)
            self.output_control.print(self.output_control.INIT, ('Transcriber',))
        except Exception as e:
            self.output_control.print(self.output_control.TRANSC_NOT_INIT, ('Transcriber', str(e)))
            sys.exit()


    def init_executor(self):
        '''
        Initiates a new executor.
        '''
        self.output_control.print(self.output_control.INIT_ATT, ('executor',))
        try:
            self.executor = Executor(self.output_control, self.database)
            self.output_control.print(self.output_control.INIT, ('Executor',))
        except Exception as e:
            self.output_control.print(self.output_control.NOT_INIT, ('Executor', str(e),))
            sys.exit()

    def __init__(self, settings_path, output_control):
        self.output_control = output_control
        oc = output_control
        self.file_handler = FileHandler(output_control)
        self.settings_dict = self.file_handler.load_from_file(settings_path)
        self.input_control = InputControl(output_control)
        ic = self.input_control
        languages_path = ('{0}{1}'.format(self.settings_dict['languages_dir'], self.settings_dict['languages_filename']))
        self.languages_dict = self.file_handler.load_from_file(languages_path)  
        audio_path = ('{0}{1}'.format(self.settings_dict['audio_dir'], self.settings_dict['audio_filename']))
        self.audio_settings_dict = self.file_handler.load_from_file(audio_path)  
        self.set_database_path()
        self.set_modules_and_commands()

        self.init_database()
        self.init_listener()
        self.init_command_finder()
        self.init_transcriber(self.command_finder.expected_calls)
        self.init_executor()

        self.exit = False
        while not self.exit:
            self.listener.record()
            alternatives = self.transcriber.transcribe(self.listener.file_path)
            print(str(alternatives))
            confidence = 0.3
            transcript = ''
            for alternative in alternatives:
                if alternative.confidence > confidence:
                    transcript = alternative.transcript
                    confidence = alternative.confidence
            response = ic.format_input(transcript)
            print('response after formating: {0}'.format(response))
            self.command_finder.find_commands(response)
            args = self.command_finder.command_args
            noninitial_responses = self.database.cursor.execute(self.database.query_list.select_responses_by_command_id.text, (str(self.command_finder.command_id), 1, 100)).fetchall()
            for noninitial_response in noninitial_responses:
                if noninitial_response[0]>25 and noninitial_response[0]<50:
                    print(noninitial_response[1])
                    self.listener.record()
                    alternatives = self.transcriber.transcribe(self.listener.file_path)
                    response = ic.format_input(alternatives[0].transcript)
                    args = args + (response,)

            self.executor.execute_command(self.command_finder.command_id, args)
            self.database.connection.commit()
            self.exit = True

        self.database.connection.close()
        self.output_control.print(self.output_control.DB_CON_CLOSED)