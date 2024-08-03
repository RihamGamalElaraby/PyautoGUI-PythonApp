"""
import time

import pyautogui

pyautogui.click(21,751)
screen_size = pyautogui.size()
print(f"Screen size: {screen_size}")
pyautogui.move(200,168)
time.sleep(2)
print(pyautogui.position())
#Point(x=56, y=33)
sleep(2)
pyautogui.doubleClick(56 , 33)
"""
import time

import pyautogui

time.sleep(1)
pyautogui.click(69, 750)
path = 'C:\\Users\\mohamed\\AppData\\Local\\Programs\\Python\\Python311\\Scripts'
pyautogui.write(path)
time.sleep(2)
pyautogui.press('enter')
# 851,62cmd
time.sleep(1.5)
pyautogui.click(851, 62)
pyautogui.write('cmd')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
install = 'pip install pyautogui'
pyautogui.write(install)


 