import pyautogui
import time
from .utils import CaptureWin as cw
from src.utils import CalibrateWin as cal

#x, y= pyautogui.locateCenterOnScreen('./img/tecla7.png',confidence=0.9)
#active windowns
def App():
    
    # preparar ventana del juego
    cw('Ikov - gamesipson')
    
    #calibramos que vea al norte el juego
    cal()
    
    status = (cw('Ikov - gamesipson') and cal())
    
    return status
    
    