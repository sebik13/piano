from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  471 Y:  450 RGB: (0, 0, 0)
#X:  594 Y:  450 RGB: (0, 0, 0)
#X:  677 Y:  450 RGB: (0, 0, 0)
#X:  763 Y:  450 RGB: (0, 0, 0)

def click(x,y) :
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(471, 450)[0] == 0:
        click(471, 450)
    if pyautogui.pixel(594, 450)[0] == 0:
        click(594, 450)
    if pyautogui.pixel(677, 450)[0] == 0:
        click(677, 450)
    if pyautogui.pixel(763, 450)[0] == 0:
        click(763, 450)    
