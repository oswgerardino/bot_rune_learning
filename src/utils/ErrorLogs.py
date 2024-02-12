
import logging

# configuracion
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')    
#archivo del log
file_handler = logging.FileHandler('loginfo.log')

# Configurar el formato del registro para el manejador de archivos
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))    

# Agregar el manejador de archivos al registro
logging.getLogger('').addHandler(file_handler)
              
def ErrorLogs(msg='',tipo='error'):
    if tipo == 'info':
        logging.info(msg)        
    elif tipo == 'warning':
        logging.warning(msg)
    else:
        logging.error(msg)       