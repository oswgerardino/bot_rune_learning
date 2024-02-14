import pyautogui

def GetCaptureRegion(left, top, width, height):       
    
    # Captura la región especificada
    screenshot = pyautogui.screenshot(region=(int(left), int(top), int(width), int(height)))

    # Guarda la captura de pantalla en un archivo (opcional)
    screenshot.show('captura_region.png')