#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 06:17:41 2020

@author: fernando
"""


import cgi
import cgitb
import configApp
cgitb.enable()


def main():
    """Docstring"""
    form = cgi.FieldStorage()
    campos = form.keys()
    campos = sorted(campos)
    pa = ''
    parametros = []
    for ele in campos:
        if ele == '000_PA':
            pa = form.getvalue(ele)
        else:
            a = form.getvalue(ele)
            parametros.append(a)
    db = configApp.mariaDB.SQL()
    db.pathcfg = '../electricAr.cfg'
    db.VerificarConexion()
    db.PA = pa
    db.parametros = parametros
    db.Registrar()
    sitio.h5 = str(db.error)
    sitio.h6 = str(db.info)
    print(sitio.Html(sitio.BodySimple()))
    print(pa, "\n", parametros)


try:
    sitio = configApp.html5.HTML5()
    sitio.lang = "es"
    sitio.keywords = 'sitio, prueba'
    sitio.author = 'Fernando Orge'
    sitio.CSS = 'css/HojaEstilo.css'
    sitio.charset = 'UTF-8'
    sitio.viewport = 'width=device-width, initial-scale=1.0'
    sitio.refresh = '120'
    sitio.nombreAp = 'ProbAr'
    sitio.eslogan = 'Sitio de prueba.'
    sitio.title = sitio.nombreAp + ' | ' + sitio.eslogan
    sitio.description = sitio.title
    sitio.legendtxt = 'Título del formulario'
    main()

except ImportError:
    cgi.print_exception()
