#!/bin/bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3.8 venv
source venv/bin/activate
pip install --upgrade pip