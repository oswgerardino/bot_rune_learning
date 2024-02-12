import pyautogui

def Config():
    #escape controlado
    pyautogui.FAILSAFE=True
    
    #win config
    width = 800
    height = 600
    
    #initial position
    x=0
    y=0
    
    return {
        'width': width,
        'height': height,
        'x': x,
        'y': y
    }