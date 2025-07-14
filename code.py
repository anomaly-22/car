# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)
steer = 0
# Create a servo object, my_servo.
drive_servo = servo.Servo(pwm)
steer_servo = servo.Servo(pwm2)



while True:
    def steerLeft():
        steer_servo.angle = 0
    def steerRight():
        steer_servo.angle = 180
    def forward():
        drive_servo.angle = 50
    def reverse():
        drive_servo.angle = 180
    def steerNeutral():
        steer_servo.angle = 90
    


    