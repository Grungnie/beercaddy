import serial

import logging
logging.getLogger()


class ArduinoSerial(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.01)

    @staticmethod
    def _calcCheckSum(msgByte):
        check = 0
        for i in msgByte:
            check = ArduinoSerial._AddToCRC(i, check)
        return check

    @staticmethod
    def _AddToCRC(b, crc):
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

    @staticmethod
    def _Str2ByteArray(msg):
        b = bytearray()
        b.extend(map(ord, msg))
        logging.debug('ByteArray: {}'.format(b))
        return b

    def send_serial_message(self, message, command):
        if type(message) is str:
            send_array = bytearray([58, len(message), command]) + bytearray(message, encoding='ascii')
        else:
            send_array = bytearray([58, len(message), command]) + message
        logging.info('sending message')
        checksum = ArduinoSerial._calcCheckSum(send_array)
        send_array.append(checksum)
        result = self.ser.write(send_array)
        logging.info('{} bytes written'.format(result))

    def read_serial_message(self):
        recieved_data = []

        if not self.ser.in_waiting:
            return None
        else:
            logging.debug('Receiving data')

        byte = self.ser.read()

        if byte == b'\x3A':
            length = int.from_bytes(self.ser.read(), byteorder='little')
            command = int.from_bytes(self.ser.read(), byteorder='little')

            for _ in range(length):
                recieved_data.append(self.ser.read())

            checksum = int.from_bytes(self.ser.read(), byteorder='little')

            logging.debug('Message Length: {}'.format(length))
            logging.debug('Message Command: {}'.format(command))
            logging.debug('Raw Message {}'.format(recieved_data))
            logging.debug('Message Checksum: {}'.format(checksum))

        else:
            logging.debug('Received unexpected character - {}'.format(int.from_bytes(byte, byteorder='little')))
            return

        try:
            string_message = ''.join([x.decode('ascii') for x in recieved_data])
            logging.debug('Message: {}'.format(string_message))
        except UnicodeDecodeError:
            logging.debug('Failed to decode message, UnicodeDecodeError')
            return

        message_bytearray = bytearray([58, length, command]) + bytearray(string_message, encoding='ascii')
        calculated_checksum = self._calcCheckSum(message_bytearray)
        logging.debug('Calculated Checksum: {}'.format(calculated_checksum))

        if checksum != calculated_checksum:
            logging.debug('Checksum Failed')
            return

        if command == 1:
            logging.info('Log Message - ' + string_message)
        else:
            logging.debug('Command Not Found')

        return string_message