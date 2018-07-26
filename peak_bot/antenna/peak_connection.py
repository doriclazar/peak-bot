import requests

class PeakConnection():
    def reqest_command(self):
        # Switch to HTTPS on BETA
        command_url = ('http://{0}/{1}'.format(self.server_url, 'command/download'))
        response = requests.get(url=update_url, params=self.params)
        return response.json()

    def check_for_updates(self):
        # Switch to HTTPS on BETA
        update_url = ('http://{0}/{1}'.format(self.server_url, 'update_check'))
        response = requests.get(url=update_url, params=self.params)
        return response.json()

    def __init__(self, output_control, bot_data, connection_data):
        self.output_control = output_control
        self.params = dict(
            bot_name=bot_data[0],
            current_version=bot_data[1],
            connection_code=connection_data[0]
        )
        self.server_ip = connection_data[1]
