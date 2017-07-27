__author__ = 'Matthew'

import requests
from python import Robot
import subprocess

if __name__ == '__main__':
    r = requests.get('https://raw.githubusercontent.com/Grungnie/microsoftbotframework/master/README.md')
    print(r.text)

    subprocess.call('touch imworking')

    robot = Robot()

    # start main loop

    print('Main')