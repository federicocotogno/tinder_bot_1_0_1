import pyautogui as pt
from time import sleep
import sys

from tinder.code_bot import Tinder

print("Starting Tinder bot...")
sleep(1)


tn = Tinder(0, 0)
tn.navigate_to_next_picture(.3)
pt.click(clicks=3, interval=.3)

sys.exit(0)

tn.navigate_to_x(.3)
tn.navigate_to_heart(.3)
tn.navigate_to_info(.3)
pt.click()
sleep(2)
tn.navigate_to_down(.3)
pt.click()

