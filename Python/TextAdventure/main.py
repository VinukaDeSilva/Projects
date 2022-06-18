# Importing the modules
import time
import sys


# Defining the delay print function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


"""
Defining the small sections of the code.
These will later be used to create the main function.
"""


def startup():
    delay_print(
        "Welcome to the Text Adventure game!"
    )
    time.sleep(1)
    delay_print(
        "If you would like to play, please press the 'p' key."
    )
    doYouWannaPlay = input()
    if doYouWannaPlay == "p":
        delay_print(
            "You have chosen to play."
        )
        time.sleep(1)
    else:
        delay_print(
            "You have chosen to exit."
        )
        time.sleep(1)
        sys.exit()


startup()
