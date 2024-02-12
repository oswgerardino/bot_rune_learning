import pygetwindow as gw
import time
from src.utils.ErrorLogs import ErrorLogs as msglog
from src.config import Config

def CaptureWin(title):
    
    config = Config()

    time.sleep(1)

    # Título de la ventana que deseas seleccionar
    window_title = title

    # Obtener todas las ventanas abiertas
    all_windows = gw.getWindowsWithTitle(window_title)
    # Buscar la ventana por su título
    target_window = None
    for window in all_windows:
        if window.title == window_title:
            target_window = window
            break

    # Si se encontró la ventana, realizar acciones sobre ella
    if target_window:    
        # Traer la ventana al frente de todas las demás
        target_window.activate()
        # Mover la ventana a la esquina superior izquierda de la pantalla
        target_window.moveTo(config['x'], config['y'])
        # Cambiar el tamaño de la ventana a 800x600
        target_window.resizeTo(config['width'], config['height'])
        msglog("¡Ventana encontrada y modificada con éxito!", 'info')
        
        return True
        
    else:
        msglog("¡Ventana no encontrada!", 'warning')
        
    return False