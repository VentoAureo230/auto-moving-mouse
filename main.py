import pyautogui as pag
import random
import time

while True:
    x = random.randint(10, 1080)
    y = random.randint(10, 1920)
    t = random.uniform(0.1, 0.9)
    pag.moveTo(x, y, t)
    time.sleep(2)
