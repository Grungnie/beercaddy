__author__ = 'Matthew'

import traceback
from arduinoserial import ArduinoSerial
from time import time, sleep

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.INFO)

if __name__ == '__main__':
    try:
        ser = ArduinoSerial()

        last_command = 0
        current_motor = 2

        while True:
            now = time()
            ser.read_serial_message()

            #ser.send_serial_message('Hey', 1)

            if last_command < now - 1:
                last_command = now
                ser.send_serial_message(bytearray([0]), current_motor)
                current_motor += 1
                if current_motor > 5:
                    current_motor = 2
                ser.send_serial_message(bytearray([255]), current_motor)

    except Exception:
        logging.warning(traceback.format_exc())
