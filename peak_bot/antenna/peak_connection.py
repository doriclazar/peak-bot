import requests

class PeakConnection():
    def reqest_command(self, command_code):
        # Switch to HTTPS on BETA
        request_url = ('http://{0}/{1}/{2}/{3}/'.format(self.server_ip, 'library/commands', command_code,'download'))
        login_url = ('http://{0}/{1}/'.format(self.server_ip, 'accounts/login'))
        session = requests.Session()
        session.get(login_url)
        self.data['csrfmiddlewaretoken']=session.cookies['csrftoken']
        response = session.post(url=request_url, data=self.data, headers={'referer':login_url, 'Connection':'close'})
        return response.json()

    def check_for_updates(self):
        # Switch to HTTPS on BETA
        request_url = ('http://{0}/{1}'.format(self.server_ip, 'update_check'))
        print('Sending request to: {0} with params: {1}'.format(request_url, self.params))
        response = requests.post(url=request_url, params=self.params)
        return response.json()

    def __init__(self, output_control, bot_data, connection_data):
        self.output_control = output_control
        self.data = dict(
            bot_name=bot_data[0],
            current_version=bot_data[1],
            connection_code=connection_data[0],
        )
        self.server_ip = connection_data[1]
