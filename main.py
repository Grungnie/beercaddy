__author__ = 'Matthew'

import traceback
from arduinoserial import ArduinoSerial
from time import time, sleep

import logging
logging.basicConfig(filename='../beercaddy.log', level=logging.INFO)

if __name__ == '__main__':
    try:
        ser = ArduinoSerial()

        last_command = time()
        last_motor = time()
        current_motor = 2
        last_motor = 5

        while True:
            now = time()
            ser.read_serial_message()

            if last_motor < now - 1:
                last_motor = now

                last_motor = current_motor

                current_motor += 1
                if current_motor > 5:
                    current_motor = 2

            if last_command < now - 1:
                last_command = now

                ser.send_serial_message(bytearray([0]), last_motor)
                ser.send_serial_message(bytearray([255]), current_motor)

    except Exception:
        logging.warning(traceback.format_exc())
