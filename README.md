# Peak Bot
Lightweight, voice-assistant-like AI. This is a young client part of the djago based multi-project "Peaks" .
"Peaks" are, simplified, social networks for bots. Places where personaly customized and trained bots exchange/trade commands.
Peak-63 and Peak-30 are in development, and should be publised along with extented features of the client part.

## Status
Peak Bot is a young sub-project. It runs well on Linux and Windows,
but still lacks large amount of features to be competitive with commercial AIs.

## Getting started
This, is written in python3, and uses sqlite3 to store it's data.
Default input and settings are using .JSON format.
It currently uses Google's Speech-to-Text Client Library for python and requires internet connection.

### Prerequisites
To satisfy the current dependencies, make sure you have python3 and pip3 installed:

#### Arch Linux
` sudo pacman -S python python-pip `

#### Ubuntu, Debian, Linux Mint
` sudo apt-get install python3 python3-pip `

#### Fedora, CentOS
` sudo yum -y install python36 python36-setuptools
  cd /usr/lib/python3.6/site-packages/
  python3 easy_install.py pip3 `

#### Windows
Download and install the latest release of the python3 from 
If PowerShell or Command Prompt don't recognize pip3 command,
add the location of the pip script to a PATH variable. 
Scripts directory should be inside the python installation.
Run ` where python ` to find it. 

Use pip3 to install google-cloud-api:

` pip3 install --upgrade google-cloud-speech `

You will also need to export the path to the google credentials.
On linux, add this line to your .bashrc:

` export GOOGLE_APPLICATION_CREDENTIALS="/some_directory/google_speech_api_credentials.json" `

and run:

` source .bashrc `

### Installing
Peak Bot is still not on PyPi, so you'll have to Clone, Curl, or Wget it from github... 

` git clone https://github.com/doriclazar/peak-bot.git 
  cd peak-bot `

### Runnig
No suprises here. Run main.py with python3, (optional) with the level of verbosity:

` python3 main.py ` or ` python3 main.py (0-6) `.
