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

        if bytes(serial_data) == b'\xff':
            break
        else:
            recieved_data.append(serial_data)

    if recieved_data[0] == b'\x00':
        logging.debug(''.join([x.decode('ascii') for x in recieved_data[1:]]))


if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600)

        while True:
            read_serial_message()
            time.sleep(0.1)


    except Exception as e:
        print(e)
        logging.warning(e)
