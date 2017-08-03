__author__ = 'Matthew'

import requests
from robot import Robot
import time
import serial
import traceback

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.DEBUG)

import binascii


def calcCheckSum(incoming):
    msgByte = Str2ByteArray(incoming)
    check = 0
    for i in msgByte:
        check = AddToCRC(i, check)
    return check


def AddToCRC(b, crc):
    b2 = b
    if (b < 0):
        b2 = b + 256
    for i in range(8):
        odd = ((b2^crc) & 1) == 1
        crc >>= 1
        b2 >>= 1
        if (odd):
            crc ^= 0x8C # this means crc ^= 140
    return crc


def Str2ByteArray(msg):
    b = bytearray()
    b.extend(map(ord, msg))
    return b


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

    calculated_checksum = calcCheckSum(':' + chr(command) + chr(length) + string_message)
    logging.debug('Calculated Checksum: {}'.format(calculated_checksum))

    if checksum != calculated_checksum:
        logging.debug('Checksum Failed')
        return

    if command == 1:
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
