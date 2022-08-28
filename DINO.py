import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time



def press(key):
    pyautogui.keyDown(key)
    return

def isCollision(Data):
# Check colison for birds
    for i in range(470,500):
        for j in range(260,270):
            if data[i, j] < 171:
                press("down")
                return
 # Check colison for cactus
    for i in range(470,520):
        for j in range(280,310):
            if data[i, j] < 200:
                press("up")
                return
    return

if __name__ =="__main__":
    time.sleep(5)
    press("up")


    while True:
        image=ImageGrab.grab().convert("L")
        data=image.load()
        isCollision(data)


#
# #         drawing rectangle wsfor the  cactus
#         for i in range(480,530):
#             for j in range(280,310):
#                 data[i,j]=0
#
# #         drawing rectangle for the birds
#         for i in range(480,510):
#             for j in range(260,270):
#                 data[i,j]=171
#
#         image.show()
#         break
#






