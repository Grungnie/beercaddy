from unittest import TestCase

from robot import Robot

class RobotTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test default
    def test_default_load(self):
        robot = Robot()

        self.assertEqual(robot.right_motor_speed, 0)
        self.assertEqual(robot.left_motor_speed, 0)
        self.assertEqual(robot.formatted_serial_data, [])

    def test_bad_motor_values(self):
        robot = Robot()

        with self.assertRaises(Exception):
            robot.set_motor_speed(0, 2000)

        with self.assertRaises(Exception):
            robot.set_motor_speed(2000, 0)

        with self.assertRaises(Exception):
            robot.set_motor_speed(-2000, 0)

        with self.assertRaises(Exception):
            robot.set_motor_speed(-2000, -2000)

        with self.assertRaises(Exception):
            robot.set_motor_speed()

    def test_set_motor_values(self):
        robot = Robot()

        robot.set_motor_speed(200, 200)
        self.assertEqual(robot.right_motor_speed, 200)
        self.assertEqual(robot.left_motor_speed, 200)

        robot.set_motor_speed(500)
        self.assertEqual(robot.right_motor_speed, 200)
        self.assertEqual(robot.left_motor_speed, 500)

        robot.set_motor_speed(right_motor_speed=1000)
        self.assertEqual(robot.right_motor_speed, 1000)
        self.assertEqual(robot.left_motor_speed, 500)

        robot.set_motor_speed(left_motor_speed=-1000)
        self.assertEqual(robot.right_motor_speed, 1000)
        self.assertEqual(robot.left_motor_speed, -1000)

        robot.set_motor_speed(0, 0)
        self.assertEqual(robot.right_motor_speed, 0)
        self.assertEqual(robot.left_motor_speed, 0)
