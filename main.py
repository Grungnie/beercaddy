__author__ = 'Matthew'

import traceback
from arduinoserial import ArduinoSerial

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.INFO)

if __name__ == '__main__':
    try:
        ser = ArduinoSerial()

        while True:
            ser.read_serial_message()

    except Exception:
        logging.warning(traceback.format_exc())
