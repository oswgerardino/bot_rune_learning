import pyautogui
from ..const.images import logs as log
from .ErrorLogs import ErrorLogs as msglog

def CountItemsIventory(image):
    
    result = list(pyautogui.locateAllOnScreen(log['simple']['1'], confidence=.9))
    cantidad_elementos = len(result)
    msglog(f'Cantidad encontrada en inventario: {cantidad_elementos}', 'info')
    
    return cantidad_elementos
