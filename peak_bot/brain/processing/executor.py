import sqlite3
import subprocess
class Executor:
    returned_args=()
    executed = False

    def __init__(self, output_control, database, modules_path):
        self.output_control = output_control
        self.database = database
        self.modules_path = modules_path

    def install_external_module(self, external_module):
        try:
            import requests
            if requests.get('http://pypi.python.org/pypi/{}/json'.format(external_module)).status_code == 200:
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
                exec('from {} import *'.format(external_module[0]), globals())
                oc.print(oc.MOD_IMPORT, external_module)
            except ImportError as e:
                oc.print(oc.MOD_NOT_IMPORT, (external_module, str(e)))
                if internet_mode:
                    install_external_module(external_module)



    def execute_command(self, command_id, command_args):
        self.executed=False
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
                    self.answer = None


                    #if it has a script path
                    if len(command[3])>0:
                        exec('from {}.{} import {}'.format(self.modules_path, command[3], command[4]))
                        exec('self.instance = {}()'.format(command[4]))
                        exec('self.answer = self.instance.{}({})'.format(definition, command_args))
                        answer_text = self.answer[0]
                        self.output_control.print(oc.ANSWER, (answer_text,))

                    else:
                        exec(definition.format(*command_args))
                        print(self.returned_args)

                    if self.answer:
                        if len(self.answer)>1:
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

                self.executed = True
                oc.print(oc.COM_EXEC)

            #except Exception as e:
            else:
                pass
                #oc.print(oc.COM_NOT_EXEC, (str(e),))
