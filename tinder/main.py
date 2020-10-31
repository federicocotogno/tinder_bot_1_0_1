import pyautogui as pt
from time import sleep
import pyperclip
import random

print("Starting Tinder bot...")
sleep(1)


class Tinder:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate_to_heart(self, speed):
        position = pt.locateOnScreen("tinder/heart.png", confidence=.8)
        self.x = position[0] + 35
        self.y = position[1] + 35
        pt.moveTo(self.x, self.y, duration=speed)
        print("Navigating to heart...")
        sleep(.5)

    def navigate_to_x(self, speed):
        position = pt.locateOnScreen("tinder/x.png", confidence=.8)
        self.x = position[0] + 20
        self.y = position[1] + 20
        pt.moveTo(self.x, self.y, duration=speed)
        print("Navigating to X...")
        sleep(.5)

    def navigate_to_info(self, speed):
        position = pt.locateOnScreen("tinder/heart.png", confidence=.8)
        self.x = position[0]
        self.y = position[1] - 50
        pt.moveTo(self.x, self.y, duration=speed)
        print("Navigating to Info...")
        sleep(.5)

    # Make sure screen is not in animation or software will not recognise precise position
    def navigate_to_down(self, speed):
        position = pt.locateOnScreen("tinder/down.png", confidence=.8)
        self.x = position[0] + 20
        self.y = position[1] + 20
        pt.moveTo(self.x, self.y, duration=speed)
        print("Navigating to Down...")
        sleep(.5)


tn = Tinder(0, 0)

tn.navigate_to_x(.3)
tn.navigate_to_heart(.3)
tn.navigate_to_info(.3)
pt.click()
sleep(2)
tn.navigate_to_down(.3)
