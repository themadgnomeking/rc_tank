#!/usr/bin/env/ python3

__author__ = "Tims Guynes"
__version__ = "0.1.0"


import pigpio
import time
import curses


pi = pigpio.pi()

stdscr = curses.initscr()

curses.cbreak()
curses.noecho()
stdscr.keypad(1)
stdscr.timeout(100)
stdscr.refresh()

key = ''
left = 0
right = 0

pwmMax = 1700
pwmMin = 1300

leftPwm = 1500
rightPwm = 1500

pi.set_servo_pulsewidth(23, 1500)
pi.set_servo_pulsewidth(24, 1500)

while key != ord('q'):

    key = stdscr.getch()

    stdscr.erase()
    stdscr.refresh()

    if key == curses.KEY_UP:
            #leftPwm = pwmMax #if motors are going the same direction
            leftPwm = pwmMin #attempt to invert the movement
            rightPwm = pwmMax

    elif key == curses.KEY_DOWN:
            #leftPwm = pwmMin #if motors are going the same direction
            leftPwm = pwmMax #invert movement
            rightPwm = pwmMin

    elif key == curses.KEY_RIGHT:
            #leftPwm = pwmMax #if motors are going the same direction
            leftPwm = pwmMin #invert the direction to correct 
            rightPwm = pwmMin

    elif key == curses.KEY_LEFT:
            #leftPwm = pwmMin #if motors are going the same direction
            leftPwm = pwmMax
            rightPwm = pwmMax

    elif key == curses.KEY_NPAGE:
        pwmMax = pwmMax - 100

    elif key == curses.KEY_PPAGE:
        pwmMax = pwmMax + 100

    elif key == curses.KEY_END:
        pwmMin = pwmMin - 100

    elif key == curses.KEY_HOME:
        pwmMin = pwmMin + 100

    elif key == -1:
        leftPwm = 1500
        rightPwm = 1500

    pi.set_servo_pulsewidth(23, leftPwm)
    pi.set_servo_pulsewidth(24, rightPwm)

    stdscr.addstr(1, 20, "pwmMax = " + str(pwmMax))
    stdscr.addstr(2, 20, "pwmMin = " + str(pwmMin))

curses.endwin()
