

class Robot(object):
    def __init__(self):
        self.left_motor_speed = 0
        self.right_motor_speed = 0
        self.formatted_serial_data = []

    def set_motor_speed(self, left_motor_speed=None, right_motor_speed=None):
        if left_motor_speed is not None and -1028 < left_motor_speed < 1028:
            self.left_motor_speed = left_motor_speed
        else:
            raise(Exception('left motor ({}) is out of motor speed bounds. It has to be between -1028 and 1028'.format(left_motor_speed)))

        if right_motor_speed is not None and -1028 < right_motor_speed < 1028:
            self.right_motor_speed = right_motor_speed
        else:
            raise(Exception('right motor ({}) is out of motor speed bounds. It has to be between -1028 and 1028'.format(right_motor_speed)))

        if left_motor_speed is None and right_motor_speed is None:
            raise(Exception('No speed was set for either motor'))

    def send_data(self):
        self._format_data()
        self._send_to_arduino()

    def _format_data(self):
        self.formatted_serial_data = [self.left_motor_speed, self.right_motor_speed]

    def _send_to_arduino(self):
        pass
