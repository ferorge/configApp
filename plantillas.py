#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .html5 import HTML5
et = HTML5()


def edesur(et):
    et.footer = et.formato('footer', et.formato('h6', et.h6) +
                           et.formato('figure',
                                      et.formato('img', et.gpl3[0]) +
                                      et.formato('figcaption', et.gpl3[1])))
    et.article = et.formato('article', et.formato('h5', et.h5) +
                            et.Tabla())
    et.section = et.formato('section', et.formato('h4', et.h4) + et.article)
    et.aside = et.formato('aside', et.formato('h3', et.h3))
    et.nav = et.formato('nav', et.formato('h2', et.h2))
    et.header = et.formato('header', et.formato('h1', et.h1))
    et.body = et.formato('body', et.header +
                         et.nav +
                         et.aside +
                         et.section +
                         et.footer)
    et.head = et.formato('head', et.formato('title', et.title) +
                         et.formato('link', 'stylesheet') +
                         et.formato('meta', 'charset') +
                         et.formato('meta', 'refresh') +
                         et.formato('meta', 'description') +
                         et.formato('meta', 'keywords') +
                         et.formato('meta', 'author') +
                         et.formato('meta', 'viewport'))
    et.html = et.formato('html', et.head + et.body)
    tmp_edesur = et.apachepy(et.doctype + et.html)
    return tmp_edesur


# Programa principal


try:
    if __name__ == '__main__':
        try:
            from configApp import eventos
            log = eventos('plantillas')
            log.debug('plantillas.py ejecutado')
        except:
            import sys
            import logging
            logging.basicConfig(filename='logs/plantillas.log',
                                level=logging.ERROR,
                                format='%(asctime)s - %(name)s - \
                                %(levelname)s - %(message)s')
            logging.error('Error de ejecucion')
            logging.error(sys.exc_info())
    else:
        pass
#        print("Content-type:text/html;charset=UTF-8\r\n\r\n")
### Devuelve error ###
#        from .__init__ import eventos
#        log=eventos('plantillas')
#        log.debug('plantillas.py importado')
except ImportError:
    print('error al importar plantillas.py')
