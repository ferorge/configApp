#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import logging
from .html5 import *
from .mariaDB import *
from .plantillas import *


class eventos:
    def __init__(self, modulo):
        self.directorio = 'logs/'
        self.fichero = self.directorio + modulo + '.log'
#        logging.basicConfig(filename=self.fichero, level=logging.DEBUG,
#            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
    def config():
        self.fichero = self.directorio + modulo + '.log'
        logging.basicConfig(filename=self.fichero, level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        return print(self.fichero)
    
    def debug(self, mensaje):
        logging.debug(mensaje)
    
    def info(self, mensaje):
        logging.info(mensaje)
    
    def warning(self, mensaje):
        logging.warning(mensaje)
    
    def error(self, mensaje):
        logging.error(mensaje)
    
    def critical(self, mensaje):
        logging.critical(mensaje)
    
# Programa principal
try:

    if __name__ == '__main__':
        try:
            instancia = eventos('configApp')
            instancia.debug('__init__.py ejecutado.')
        except 'Error de ejecucion':
            import sys
            instancia = eventos('configApp')
            instancia.error(sys.exc_info())
    else:
#        import html5, mariaDB, plantillas
#        logging.basicConfig(filename='logs/configApp.log', level=logging.DEBUG,
#            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#        logging.debug('importado.')
        pass
except ImportError:
    print('error al importar __init__.py')
 
