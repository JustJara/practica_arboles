'''
Este modulo es el encargado de ejecutar la aplicacion
'''

import sys

sys.path.append('src')

from src.console_view.console_UI import ConsoleUI

if __name__ == '__main__':
    ui = ConsoleUI()
    ui.run_app()
