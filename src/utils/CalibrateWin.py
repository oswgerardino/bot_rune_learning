import pyautogui
import time
from .GetCapture import GetCapture
from src.const import posiciones as pos
from src.const import colores as color
from src.utils.ErrorLogs import ErrorLogs as msglog
from src.const.images import interface as intf


def CalibrateWin():
    
    #primero hacemos click en la posicion del pixel del compass
    pyautogui.click(pos['compass']['x'],pos['compass']['y'], duration=1)
        
    # Color que estamos buscando
    color_deseado = (color['compass']['r'], color['compass']['g'], color['compass']['b'])

    # Verifica si el color del píxel en las coordenadas (x, y) coincide con el color deseado
    
    if pyautogui.pixelMatchesColor(pos['compass']['x'],pos['compass']['y'], color_deseado):
        msglog("El color en la posición especificada coincide con el color deseado.",'info')
        
        GetCapture(pos['compass']['x'],pos['compass']['y'], 100, 100)
        
        pyautogui.click(pos['compass']['x'],pos['compass']['y'], duration=1)
        
        # Verifica si la imagen está presente en la pantalla
        if pyautogui.locateCenterOnScreen(intf['minimap']['compass'], confidence=0.9, region=(500,0, 200, 100)) is not None:
            msglog("Imagen encontrada.",'info')
            # Agrega aquí tu código especial si la imagen y el color coinciden
            return True
        else:
            msglog("Imagen no encontrada.",'warning')
            # Agrega aquí tu código de manejo de errores si la imagen no coincide
            
    else:
         msglog("El color en la posición especificada NO coincide con el color deseado.",'warning')
        # Agrega aquí tu código de manejo de errores si el color no coincide

    
    #encontrar compass
    x,y = pyautogui.locateCenterOnScreen(intf['minimap']['compass'], grayscale=True, confidence=0.9, region=(500,0, 200, 100))
    time.sleep(1)
    #click en compass para colocar la pantalla en una posicion norte
    pyautogui.moveTo(x,y,duration=.5)

    return False