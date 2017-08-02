__author__ = 'Matthew'

import requests
from robot import Robot
import time
import serial

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.DEBUG)


def read_serial_message():
    recieved_data = []
    recieving = True

    while recieving:
        serial_data = ser.read()

        if int(serial_data) == 255:
            break
        else:
            recieved_data.append(serial_data)

    logging.debug(''.join(recieved_data))


if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600)

        while True:
            read_serial_message()
            time.sleep(0.1)


    except Exception as e:
        logging.warning(e)
