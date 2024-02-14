import pyautogui
import time

def GetCaptureMouse(width, height):
    
    # Obtener la posición actual del puntero del mouse
    current_x, current_y = pyautogui.position()
    
    # Calcular las coordenadas de la esquina superior izquierda del rectángulo de captura
    capture_left = current_x - width // 2
    capture_top = current_y - height // 2
    
    # Capturar la región de la pantalla centrada en el puntero del mouse
    im = pyautogui.screenshot(region=(capture_left, capture_top, width, height))

    # Mostrar la captura de pantalla
    im.show()
    
    time.sleep(1)
    im.show()