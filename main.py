__author__ = 'Matthew'

import requests
from robot import Robot
import time
import serial
import traceback

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.DEBUG)


def read_serial_message():
    recieved_data = []

    logging.debug('Waiting for message')
    byte = ser.read()

    if byte == b'\x3A':
        length = int.from_bytes(ser.read(), byteorder='little')
        command = int.from_bytes(ser.read(), byteorder='little')

        for _ in range(length):
            recieved_data.append(ser.read())

        checksum = ser.read()

        logging.debug('Message Command: {}'.format(command))
        logging.debug('Message Length: {}'.format(length))
        logging.debug('Raw Message {}'.format(recieved_data))
        logging.debug('Message Checksum: {}'.format(int.from_bytes(checksum, byteorder='little')))

    else:
        logging.debug('Received unexpected character - {}'.format(int.from_bytes(byte, byteorder='little')))
        return

    string_message = ''.join([x.decode('ascii') for x in recieved_data])
    logging.debug('Message: {}'.format(string_message))

    if checksum != b'\x01':
        logging.debug('Checksum Failed')
        return

    if command == 0:
        logging.info('Log Message - ' + string_message)
    else:
        logging.debug('Command Not Found')


if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600)

        while True:
            read_serial_message()

    except Exception:
        logging.warning(traceback.format_exc())
