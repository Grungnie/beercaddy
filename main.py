__author__ = 'Matthew'

import requests
from robot import Robot
import time
import logging
logging.basicConfig(filename='beercaddy.log', level=logging.DEBUG)


if __name__ == '__main__':
    r = requests.get('https://raw.githubusercontent.com/Grungnie/microsoftbotframework/master/README.md')
    print(r.text)

    robot = Robot()

    # start main loop
    counter = 0
    while True:
        with open('../test.txt', 'w+') as file:
            file.write(str(counter))
        logging.debug(counter)
        time.sleep(10)
        counter += 1
