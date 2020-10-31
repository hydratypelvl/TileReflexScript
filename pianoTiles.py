from time import sleep
import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


sleep(3)

while not keyboard.is_pressed('q'):
    # First Row
    if not pyautogui.pixelMatchesColor(640, 400, (211, 211, 211)):
        click(640, 400)
    if not pyautogui.pixelMatchesColor(735, 400, (211, 211, 211)):
        click(735, 400)
    if not pyautogui.pixelMatchesColor(830, 400, (211, 211, 211)):
        click(830, 400)
    if not pyautogui.pixelMatchesColor(925, 400, (211, 211, 211)):
        click(925, 400)

    # Second Row
    if not pyautogui.pixelMatchesColor(640, 500, (211, 211, 211)):
        click(640, 500)
    if not pyautogui.pixelMatchesColor(735, 500, (211, 211, 211)):
        click(735, 500)
    if not pyautogui.pixelMatchesColor(830, 500, (211, 211, 211)):
        click(830, 500)
    if not pyautogui.pixelMatchesColor(925, 500, (211, 211, 211)):
        click(925, 500)

    # Third Row
    if not pyautogui.pixelMatchesColor(640, 600, (211, 211, 211)):
        click(640, 600)
    if not pyautogui.pixelMatchesColor(735, 600, (211, 211, 211)):
        click(735, 600)
    if not pyautogui.pixelMatchesColor(830, 600, (211, 211, 211)):
        click(830, 600)
    if not pyautogui.pixelMatchesColor(925, 600, (211, 211, 211)):
        click(925, 600)

    # Forth Row
    if not pyautogui.pixelMatchesColor(640, 700, (211, 211, 211)):
        click(640, 700)
    if not pyautogui.pixelMatchesColor(735, 700, (211, 211, 211)):
        click(735, 700)
    if not pyautogui.pixelMatchesColor(830, 700, (211, 211, 211)):
        click(830, 700)
    if not pyautogui.pixelMatchesColor(925, 700, (211, 211, 211)):
        click(925, 700)
