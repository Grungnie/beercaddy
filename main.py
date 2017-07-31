__author__ = 'Matthew'

import requests
from python import Robot
import subprocess
import time
import os

if __name__ == '__main__':
    r = requests.get('https://raw.githubusercontent.com/Grungnie/microsoftbotframework/master/README.md')
    print(r.text)

    robot = Robot()

    # start main loop
    counter = 0
    while True:
        with open('../test8.txt', 'w+') as file:
            file.write(str(counter))
        time.sleep(10)
        counter += 1
