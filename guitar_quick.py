#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Just the imports for using nxt

import nxt.locator
from nxt.motor import *
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

print "Finding a brick..."

try:
    # Locate the brick
    b = nxt.locator.find_one_brick()
    print "Brick connected"
except:
    print "Sorry, we couldn't find a nxt brick..."
    sys.exit()

# NXT plays a tone when is ready to play

b.play_sound_file(False, 'Good.rso')

# Reset the speed control (the motor tacho count)
Motor(b, PORT_A).reset_position(True)

# If the brick has been found
if b:
    # Main while
    while True:
        # When you press the button
        if Touch(b, PORT_4).get_sample():
            Motor(b, PORT_A).run(100)
        else:
            Motor(b, PORT_A).run(0)

else:
    print 'No NXT bricks found'
