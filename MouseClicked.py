# Python Check if mouse clicked
# https://stackoverflow.com/questions/41688871/python-check-if-mouse-clicked


import win32api
import time

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
while True:
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
        else:
            print('Left Button Released')
            win32api.SetCursorPos((midWidth, midHeight))
    time.sleep(0.001)