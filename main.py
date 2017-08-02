__author__ = 'Matthew'

import requests
from robot import Robot
import time
import serial

import logging
logging.basicConfig(filename='beercaddy.log', level=logging.DEBUG)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)

    while True:
        try:
            serial_data = ser.readline()
            logging.debug(serial_data)
        except Exception as e:
            logging.warning(e)
        time.sleep(0.1)
