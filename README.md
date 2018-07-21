# Peak Bot
This voice-assistant-like AI is a young client part of the "Peaks" infrastructure.
"Peaks" are Django-based managment servers for personaly customized and trained bots, and places where they exchange/trade their commands.
Peak 63 and [Peak 30] are in development, and should be publised along with extented features of the client part.

## Table of contents
<!--ts-->
   * [Status](#status)
   * [Getting started](#getting-started)
   * [Prequisites](#prequisites)
      * [Arch Linux](#arch-linux)
      * [Ubuntu, Debian, Linux Mint](ubuntu-debian-linux-mint)
      * [Fedora, CentOS](#fedora-centos)
      * [Windows](#windows)
   * [Installation](#installation)
   * [Usage](#usage)
<!--te-->

## Status
Alpha release is now on PyPI.
Master branch runs well on Linux and Windows,
but still lacks large amount of features to be competitive with commercial AIs.
To test and/or contribute in the meantime, please follow the rest of this file...

## Getting started
Peak Bot is written in python3, and relies on sqlite3 to store it's data.
It currently uses Google's Speech-to-Text Client Library for python and requires internet connection.
Default input and settings are using .JSON format.

## Prequisites
To satisfy the current dependencies, make sure you have python3, pip3, and portaudio installed.

### Arch Linux
` sudo pacman -S python python-pip portaudio `

### Ubuntu, Debian, Linux Mint
` sudo apt-get install python3 python3-pip libportaudio2 `

### Fedora, CentOS
` sudo yum -y install python36 python36-setuptools portaudio-devel `

optional:
` cd /usr/lib/python3.6/site-packages/ `
 
` python3 easy_install.py pip3 `

### Windows
Download and install the latest python3, and portaudio releases from [python.org] and [portaudio.com].

Pip3 script should now be automaticaly placed inside 'Scripts' directory.
If PowerShell or Command Prompt don't recognize ` pip3 ` command,
run ` where python ` to find it the location of the 'Scripts', 
and add the location of the pip script to a PATH.

## Installation
Peak Bot is now on PyPi, so you should have no problems installing it with:

` pip3 install --upgrade peak-bot `

or

` easy_install peak-bot `


Before running, you will also need to export the path to the google credentials.
On linux, add this line to your .bashrc file:

` export GOOGLE_APPLICATION_CREDENTIALS="/some_directory/google_speech_api_credentials.json" `

and run:

` source .bashrc `

## Usage
If installation went well, peak-bot command should be ready...

`$ peak-bot <verbosity 0-6> `.

[Peak 30]: https://www.github.com/doriclazar/peak_30
[python.org]: https://www.python.org/downloads/windows/
[portaudio.com]: http://www.portaudio.com/download.html
