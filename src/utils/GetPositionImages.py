import pyautogui
import time

def GetPositionImages(type="", image="", left=0, top=0, width=0, height=0):
    
    if type == "locate_center":
        x, y, = pyautogui.locateCenterOnScreen(image, confidence=0.9, region=(left, top, width, height))
        
    return {
        'x': x,
        'y': y        
    }
    
    