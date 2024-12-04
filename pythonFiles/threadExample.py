from time import *
from threading import Thread
def myBox():
    while True:
        print('..............The Box is Open.')
        sleep(5)
        print('..............The Box is closed.')
        sleep(5)
def myLed():
    while True:
        print('The Led is ON.')
        sleep(1)
        print('The Led is OFF.')
        sleep(1)
boxThread=Thread(target=myBox)
ledThread=Thread(target=myLed)
boxThread.daemon=True
ledThread.daemon=True
boxThread.start()
ledThread.start()
