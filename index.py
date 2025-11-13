import cv2
import numpy as np
import pyautogui as pg
import win32api, win32con, win32gui, win32com.client
import time
import path as p
import os
import subprocess
import psutil


AcceptGame = cv2.imread("accept.png", cv2.IMREAD_UNCHANGED)
if AcceptGame is None:
    raise FileNotFoundError("Accept.png doesn't exist.")
if AcceptGame.shape[2] == 4:
    # RGBA to RGB
    AcceptGame = cv2.cvtColor(AcceptGame, cv2.COLOR_BGRA2BGR)
AcceptGame_gray = cv2.cvtColor(AcceptGame, cv2.COLOR_BGR2GRAY)

while True:
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot_gray, AcceptGame_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= 0.9:
        print("Accept button found. Clicking...")
        button_x = max_loc[0] + AcceptGame.shape[1] // 2
        button_y = max_loc[1] + AcceptGame.shape[0] // 2
        pg.click(button_x, button_y)
        time.sleep(5)  
    else:
        print("Accept button not found. Retrying...")
        time.sleep(1) 