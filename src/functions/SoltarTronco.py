
import pyautogui
import time
from ..utils import GetCaptureMouse
from ..utils.ErrorLogs import ErrorLogs as msglog
from ..const.images import logs as log
from ..const.images import texts as tx
from ..utils.GetPositionImages import GetPositionImages as getpos
from ..utils.GetitemInRegionSpecific import GetitemInRegionSpecific as getirs

def SoltarTronco():
    msglog("Soltando tronco", "info")
    
    time.sleep(2)
    #entonrar numero de elementos en coincidencia del item en la ventana
    result_item_found= getirs(log['simple']['1'], 'Ikov')
    left = result_item_found['posicion']['left']
    top = result_item_found['posicion']['top']
    width = result_item_found['posicion']['width']
    height = result_item_found['posicion']['height']
    
    #encontrar img
    result = getpos('locate_center', log['simple']['1'], left, top, width, height)
    
    #click en compass para colocar la pantalla en una posicion norte
    pyautogui.moveTo(result['x'],result['y'],duration=.5)

    #click derecho sobre el item
    pyautogui.rightClick()
    
    #identificar texto      
    result_text_found= getirs(tx['droplogs'], 'Ikov')
    
    text_left = result_text_found['posicion']['left']
    text_top = result_text_found['posicion']['top']
    text_width = result_text_found['posicion']['width']
    text_height = result_text_found['posicion']['height']
    
    result_text = getpos('locate_center', tx['droplogs'], text_left, text_top, text_width, text_height)  
    
    #mover a la opcion de drop/soltar
    pyautogui.moveTo(result_text['x'],result_text['y'],duration=.5)
    
    #seleccionamos la opcion
    pyautogui.leftClick()
    
    time.sleep(3)
          
   
    return False