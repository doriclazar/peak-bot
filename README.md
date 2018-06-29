# Peak Bot
This voice-assistant-like AI is a young client part of the "Peaks" infrastructure.
"Peaks" are Django-based managment servers for personaly customized and trained bots, and places where they exchange/trade their commands.
Peak-63 and Peak-30 are in development, and should be publised along with extented features of the client part.

## Status
Peak Bot is a young repository. Master branch runs well on Linux and Windows,
but still lacks large amount of features to be competitive with commercial AIs.
First release should be avalible by mid-Jully. 
To test and/or contribute in the meantime, please follow the rest of this file...

## Getting started
Peak Bot is written in python3, and relies on sqlite3 to store it's data.
It currently uses Google's Speech-to-Text Client Library for python and requires internet connection.
Default input and settings are using .JSON format.


### Prerequisites
To satisfy the current dependencies, make sure you have python3, pip3, portaudio, pyaudio, and google-cloud-api installed.


#### Arch Linux
` sudo pacman -S python python-pip portaudio `

` pip3 install --upgrade pyaudio google-cloud-speech `

#### Ubuntu, Debian, Linux Mint
` sudo apt-get install python3 python3-pip libportaudio2 `

` pip3 install --upgrade pyaudio google-cloud-speech `

#### Fedora, CentOS
` sudo yum -y install python36 python36-setuptools portaudio-devel `

` cd /usr/lib/python3.6/site-packages/ `
 
` python3 easy_install.py pip3 `

` pip3 install --upgrade pyaudio google-cloud-speech `

#### Windows
Download and install the latest python3, and portaudio releases from [python.org] and [portaudio.com].

Pip3 script should now be automaticaly placed inside 'Scripts' directory.
If PowerShell or Command Prompt don't recognize ` pip3 ` command,
run ` where python ` to find it the location of the 'Scripts', 
and add the location of the pip script to a PATH, or try running:

` python3 -m pip3 install --upgrade pyaudio google-cloud-speech `

### Installing
Peak Bot is still not on PyPi, so you'll have to Clone, Curl, or Wget it from github... 

` git clone https://github.com/doriclazar/peak-bot.git `

` cd peak-bot `

Before running, you will also need to export the path to the google credentials.
On linux, add this line to your .bashrc file:

` export GOOGLE_APPLICATION_CREDENTIALS="/some_directory/google_speech_api_credentials.json" `

and run:

` source .bashrc `

### Runnig
Run main.py with python3, (optional) with the level of verbosity:

` python3 main.py ` or ` python3 main.py (0-6) `.

[python.org]: https://www.python.org/downloads/windows/
[portaudio.com]: http://www.portaudio.com/download.html
