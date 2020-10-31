import pyautogui as pt
from time import sleep
import random

from tinder.code_bot import Tinder

print("Starting Tinder bot...")
heart_swipes = 0
x_swipes = 0

tn = Tinder(0, 0)

# 30 simulated swipes
for i in range(30):
    # Generates some random numbers
    random_no = random.randrange(1, 5)
    random_no_swipe = random.randrange(10)

    # Performs a simulated Tinder experience
    tn.navigate_to_next_picture(.3)
    pt.click(clicks=random_no, interval=.3)
    tn.navigate_to_info(.3)
    pt.click()
    sleep(2)
    tn.navigate_to_down(.3)
    pt.click()

    # if number is 3 or 4, it will not swipe = 20% swipe away rate
    if random_no_swipe in range(3, 5):
        tn.navigate_to_x(.3)
        pt.click()

        x_swipes += 1
    else:
        tn.navigate_to_heart(.3)
        pt.click()

        heart_swipes += 1

    # Prints some stats about current session to the user
    print(f"""--------------------
Total swipes: 
Heart = {heart_swipes} 
X = {x_swipes}
--------------------""")

    sleep(random_no)
