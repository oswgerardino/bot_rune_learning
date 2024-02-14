import time
from .utils import CaptureWin as cw
from .utils import CalibrateWin as cal
from .functions import SoltarTronco as st
from .utils import CountItemsIventory as countitem
from .const.images import logs as log
#x, y= pyautogui.locateCenterOnScreen('./img/tecla7.png',confidence=0.9)
#active windowns
def App():
    title='Ikov - gamesipson'
    # preparar ventana del juego
    #cw(title)
    
    #esperar
    #time.sleep(1)
    
    #calibramos que vea al norte el juego
    #cal()
    
    #esperar
    #time.sleep(1)
    
    #vaciamos el inventario
    
    for i in range(0,countitem(log['simple']['1'])):
        print(i)
        st()