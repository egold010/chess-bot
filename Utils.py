import pyautogui
import time
import mouse as mouse

while True:
    time.sleep(3)
    pos = pyautogui.position()
    print(pos)
    sc = pyautogui.screenshot()
    print(sc.getpixel(mouse.get_position()))