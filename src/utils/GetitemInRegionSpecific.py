import pyautogui
from .GetCaptureRegion import GetCaptureRegion
from .ErrorLogs import ErrorLogs as msglog

def GetitemInRegionSpecific(image="", title=""):
    left=""
    top=""
    width=""
    height=""
    #localizar la imagen en la ventana seleccionada
    if (pyautogui.locateOnWindow(image, title, confidence=0.9)):
        
        #cordenadas del item
        left, top, width, height = pyautogui.locateOnWindow(image, title, confidence=0.9)
        
        msglog('Se encontraron una imagen', 'info')
    
    else:
        msglog('No se encontro ninguna imagen', 'info')
    
    return {
        'posicion':{
            'left':left,
            'top':top,
            'width':width,
            'height':height
        }
    }
    
    