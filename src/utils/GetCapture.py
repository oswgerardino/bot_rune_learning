import pyautogui
import time

def GetCapture(position_left, posistion_top, width, height):
    im = pyautogui.screenshot(region=(position_left,posistion_top, width, height))
    #im.save('C:/Users/oswgerardino/Desktop/captura.png')
    time.sleep(1)
    im.show()