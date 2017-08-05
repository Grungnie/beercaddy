__author__ = 'Matthew'

import traceback
from arduinoserial import ArduinoSerial
from time import time

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.DEBUG)

if __name__ == '__main__':
    try:
        ser = ArduinoSerial()

        while True:
            now = time()
            while time() < now+1:
                ser.read_serial_message()

            ser.send_serial_message('Hey')

    except Exception:
        logging.warning(traceback.format_exc())
