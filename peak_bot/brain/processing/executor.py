import sqlite3
import subprocess
#import requests
class Executor:
    returned_args=()

    def __init__(self, output_control, database, modules_path):
        self.output_control = output_control
        self.database = database
        self.modules_path = modules_path

    def install_external_module(self, external_module):
        try:
            if requests.get('http://pypi.python.org/pypi/{0}/json'.format(external_module)).status_code == 200:
                #Prompt for installation
                pass
            else:
                self.output_control.print(self.output_control.EXT_MOD_NOT_FOUND, (external_module,))
        except TimeoutError as e:
            self.output_control.print(self.output_control.EXT_MOD_NOT_INSTALL, (str(e),))


    def import_external_modules(self, command_id):
        self.external_modules_dict = {}
        external_modules = (self.database.cursor.execute(self.database.query_list.select_external_modules_by_command_id.text, (str(command_id),))).fetchall()
        oc = self.output_control
        for external_module in external_modules:
            oc.print(oc.MOD_ATT_IMPORT, external_module)
            try:
                exec('from {0} import *'.format(external_module[0]), globals())
                oc.print(oc.MOD_IMPORT, external_module)
            except ImportError as e:
                oc.print(oc.MOD_NOT_IMPORT, (external_module, str(e)))
                if internet_mode:
                    install_external_module(external_module)



    def execute_command(self, command_id, command_args):
        oc = self.output_control
        definition = 'No command'
        external_modules = ()

        command = (self.database.cursor.execute(self.database.query_list.select_command_by_id.text, (str(command_id),))).fetchone()

        if command is not None:
            programming_language = command[1]
            definition = command[2]
            #try:
            if True:
                if programming_language == 'python3':
                    self.import_external_modules(command_id)

                    if len(command[3])>0:
                        exec('from {0}.{1} import {2}'.format(self.modules_path, command[3], command[4]))
                        exec('self.instance = {0}()'.format(command[4]))
                        exec('self.answer = self.instance.{}({})'.format(definition, command_args))
                        answer_text = self.answer[0]
                        self.output_control.print(self.output_control.ANSWER, (answer_text,))

                    else:
                        exec(definition.format(*command_args))

                    if self.answer[1]:
                        success_response = self.database.cursor.execute(
                                self.database.query_list.select_responses_by_command_id.text, 
                                (str(command_id), self.answer[1], self.answer[1])).fetchone()
                        oc.print(oc.SUC_RESP, (success_response,))

                elif programming_language == 'sql':
                    pass

                elif programming_language == 'bash':
                    subprocess.Popen(definition.format(*command_args), shell = True)

                elif programming_language == 'cpp':
                    pass

                oc.print(oc.COM_EXEC)

            #except Exception as e:
            else:
                pass
                #oc.print(oc.COM_NOT_EXEC, (str(e),))
