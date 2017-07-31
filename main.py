__author__ = 'Matthew'

import requests
from python import Robot
import subprocess
import time
import os

if __name__ == '__main__':
    robot = Robot()

    # start main loop
    counter = 0
    while True:
        with open('test.txt', 'w+') as file:
            file.write(str(counter))
        time.sleep(10)
        counter += 1
