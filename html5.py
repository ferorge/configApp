#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class HTML5:
    def __init__(self):
        '''
        Etiquetas discontinuadas en HTML5:
            - acronym.
            - applet.
            - basefont.
            - big.
            - center.
            - dir.
            - embed.
            - font.
            - frame.
            - frameset.
            - noframes.
            - object.
            - param.
            - strike.
            - tt.
        '''
        self.etiquetas = {'doctype': '',
                          'html': [0, True, 'Raíz de documento HTML.'],
                          'head': [1, True, 'Contenedor de metadatos.'],
                          'style': [1, True, 'Define información de estilo\
                                    (CSS) para un documento.'],
                          'title': [2, False, 'Se muestra en la barra de \
                                    título del navegador.'],
                          'meta': [2, False, 'Metadatos sobre un documento\
                                   HTML.'],
                          'link': [2, False, 'Enlace a recurso externo.'],
                          'noscript': [2, False, 'Texto cuando JavaScript \
                                       está deshabilitado.'],
                          'body': [1, True, 'Contenedor de documento.'],
                          'script': [3, True, 'JavaScript del lado del\
                                     cliente.'],
                          'header': [2, True, 'Encabezado del sitio.'],
                          'h1': [3, False, 'Título de primera jerarquía.'],
                          'nav': [2, True, 'Barra de navegación.'],
                          'h2': [3, False, 'Título de segunda jerarquía.'],
                          'aside': [2, True, 'Barra lateral.'],
                          'h3': [3, False, 'Título de tercera jerarquía.'],
                          'section': [3, True, 'Sección del documento.'],
                          'h4': [4, False, 'Título de cuarta jerarquía.'],
                          'main': [2, True, 'Contenido principal de un\
                                   documento.'],
                          'article': [4, True, 'Bloque independiente.'],
                          'h5': [5, False, 'Título de quinta jerarquía.'],
                          'form': [4, True, 'Formulario.'],
                          'fieldset': [5, True, 'Conjunto de campos.'],
                          'legend': [6, False, 'Título de conjunto de\
                                     campos.'],
                          'label': [6, False, 'Etiqueta de entrada.'],
                          'input': [6, False, 'Entrada'],
                          'textarea': [6, False, 'Entrada de texto\
                                       expandible.'],
                          'select': [6, True, 'Lista desplegable de \
selección.'],
                          'optgroup': [7, True, 'Grupo en opciones de \
selección.'],
                          'option': [8, False, 'Opciones de selección.'],
                          'meter': [5, False, 'Barra indicadora.'],
                          'progress': [5, False, 'Barra de progreso.'],
                          'output': [5, False, 'Resultado.'],
                          'datalist': [5, False, 'Lista de entradas \
posibles.'],
                          'button': [5, False, 'Botón formateado.'],
                          'footer': [2, True, 'Pie del sitio'],
                          'h6': [3, False, 'Título de sexta jerarquía.'],
                          'address': [3, True, 'Dirección de contacto.'],
                          'ol': [4, True, 'Lista con orden.'],
                          'ul': [4, True, 'Lista sin orden.'],
                          'li': [5, False, 'Item de lista.'],
                          'blockquote': [4, True, 'Cita larga.'],
                          'template': [4, True, 'Bloque oculto.'],
                          'figure': [3, True, 'Contendor para imagen.'],
                          'svg': [4, True, 'Contendor para gráficos SVG.'],
                          'picture': [4, True, 'Contendor para imagen.'],
                          'audio': [4, True, 'Contenedor para sonido.'],
                          'video': [4, True, 'Contenedor para video.'],
                          'source': [5, False, 'Fuente para audio, video \
y picture.'],
                          'track': [5, False, 'Pistas de texto para \
elementos <audio> o <video> .'],
                          'img':  [4, False, 'Enlace para imágen.'],
                          'a':  [4, False, 'Hipervínculo.'],
                          'figcaption': [4, False, 'Epígrafe.'],
                          'details': [4, True, 'Bloque de texto oculto.'],
                          'summary': [5, False, 'Título de bloque de \
texto oculto.'],
                          'br': [6, True, 'Salto de linea.'],
                          'hr': [5, True, 'Salto de linea con linea \
horizontal.'],
                          'div': [5, True, 'División de texto.'],
                          'p': [5, False, 'Párrafo.'],
                          'pre': [5, True, 'Texto preformateado se muestra \
                                  como está en fuente HTML.'],
                          'dialog': [5, False, 'Cuadro de texto enmarcado.'],
                          'ruby': [5, True, 'Bloque de texto rubí.'],
                          'rt': [0, False, 'Texto en una anotación rubí.'],
                          'rp': [0, False, 'Texto rubí para navegadores que \
                                 no admiten anotaciones rubí.'],
                          'dl': [5, True, 'Lista.'],
                          'dt': [6, False, 'Item de lista.'],
                          'dd': [6, False, 'Describe el item de la lista.'],
                          'data': [0, False, 'Traducción legible por máquina.'],
                          'dfn': [0, False, 'Elemento de definición.'],
                          'var': [0, False, 'Variable matemática. Itálico.'],
                          'code': [0, False, 'Código de programación. \
Fuente monoespacio.'],
                          'samp': [0, False, 'Salida de programa. \
Fuente monoespacio.'],
                          'span': [0, False, 'Color.'],
                          'bdi': [0, False, 'Aislamiento bidireccional.'],
                          'bdo': [0, False, 'Anulación bidireccional.'],
                          'sup': [0, False, 'Súperindice.'],
                          'sub': [0, False, 'Subíndice.'],
                          'kbd': [0, False, 'Entrada de teclado. \
Fuente monoespacio.'],
                          's': [0, False, 'Texto no relevante. Tachado.'],
                          'del': [0, False, 'Texto eliminado. Tachado.'],
                          'ins': [0, False, 'Texto insertado. Subrayado.'],
                          'u': [0, False, 'Texto como palabras mal escritas.\
 Subrayado.'],
                          'time': [0, False, 'Hora especifica.'],
                          'i': [0, False, 'Itálico alternativo.'],
                          'wbr': [0, False, 'Ruptura de palabra para \
agregar un salto de línea.'],
                          'mark': [5, False,'Resaltado.'],
                          'em': [5, False, 'Itálico.'],
                          'b': [5, False, 'Negrita.'],
                          'strong': [5, False, 'Negrita fuerte.'],
                          'small': [5, False, 'Pequeño.'],
                          'cite': [5, False, 'Citado.'],
                          'abbr': [5, False, 'Abreviatura.'],
                          'q': [5, False, 'Cita corta entre << >>.'],
                          'table': [5, True, 'Tabla.'],
                          'caption': [6, False, 'Título de tabla.'],
                          'thead': [6, True, 'Encabezado de tabla'],
                          'tbody': [6, True, 'Cuerpo de tabla.'],
                          'tfoot': [6, True, 'Pie de tabla.'],
                          'tr': [7, True, 'Fila de tabla.'],
                          'th': [8, False, 'Campo de encabezado de tabla.'],
                          'td': [8, False, 'Campo de dato estándar de tabla.'],
                          'colgroup': [7, True, 'Grupo de columnas de tabla.'],
                          'col': [8, False, 'Columna de tabla.'],
                          'canvas': [4, False],
                          'iframe': [4, True, 'Incrustar otro documento HTML.'],
                          'map': [4, True, 'Mapa de imagen con áreas en las \
                                  que se puede hacer clic.'],
                          'area': [5, False],
                          }
        self.doctype = "<!DOCTYPE html>" + '\n'
        self.html = 'Por favor defina el atributo html.'
        self.lang = 'Por favor defina el atributo lang.'
        self.charset = 'Por favor defina el atributo charset.'
        self.description = 'Por favor defina el atributo description.'
        self.keywords = 'Por favor defina el atributo keywords.'
        self.author = 'Por favor defina el atributo author.'
        self.viewport = 'Por favor defina el atributo viewport.'
        self.refresh = 'Por favor defina el atributo refresh.'
        self.head = 'Por favor defina el atributo head.'
        self.body = 'Por favor defina el atributo body.'
        self.title = 'Por favor defina el atributo title.'
        self.titletxt = 'Por favor defina el atributo titletxt.'
        self.CSS = 'Por favor defina el atributo CSS.'
        self.nombreAp = 'Por favor defina el atributo nombreAp.'
        self.eslogan = 'Por favor defina el atributo eslogan.'
        self.header = 'Por favor defina el atributo header.'
        self.nav = 'Por favor defina el atributo nav.'
        self.aside = 'Por favor defina el atributo aside.'
        self.main = 'Por favor defina el atributo main.'
        self.section = 'Por favor defina el atributo section.'
        self.article = 'Por favor defina el atributo article.'
        self.TablaTitulo = 'Por favor defina el atributo TablaTitulo.'
        self.TablaEncabezado = [] # Atributo para el encabezado de tabla.
        self.TablaFilas = []      # Atributo para las filas de tabla.
        self.TablaFilaPie = []    # Atributo para el pie de tabla.
        self.footer = 'Por favor defina el atributo footer.'
        self.h1 = 'Por favor defina el atributo h1.'
        self.h2 = 'Por favor defina el atributo h2.'
        self.h3 = 'Por favor defina el atributo h3.'
        self.h4 = 'Por favor defina el atributo h4.'
        self.h5 = 'Por favor defina el atributo h5.'
        self.h6 = 'Por favor defina el atributo h6.'
        self.address = 'Por favor defina el atributo address.'
        self.contacto = ['mailto:fernando.orge@tutamail.com', 'Contacto']
        self.gpl3 = ['images/gplv3.png', 
                     'Licencia', 
                     'https://www.gnu.org/licenses/gpl-3.0.en.html']
        self.liList = [] # Atributo para función li().
#        self.method = 'get'
#        self.autocomplete = 'on'
#        self.action = 'registrar.py'
        self.FormAtr= {'method': 'get',
                       'autocomplete': 'on',
                       'action' : 'registrar.py'}
        self.InputAtr= {}
        self.htmlpath = './html/' # Atributo para función exportar().
        self.htmlFile = 'main'    # Atributo para función exportar().
        self.htmlext = '.html'    # Atributo para función exportar().
        self.olStart = "1"
        self.AsideList = {}
        self.AsideListsub = {}
        self.legendtxt = 'Formulario'
        self.InputList = {}
        self.NavList = {}
    
    def identacion(self, etiqueta, idtcA, contenido, idtcC):
        '''
        Define la identacion de las etiquetas.
        Esto no es necesario para el funcionamiento del HTML,
        solo es para facilitar su lectura.
        Los condicionales if ajustan las particularidades de cada etiqueta.
        Esta función es accedida a través de la función self.formato().
        '''
        nivel = self.etiquetas[etiqueta][0]
        NuevaLinea = self.etiquetas[etiqueta][1]
        # Evalua si la etiqueta de cierre se escribe en una nueva linea.
        if NuevaLinea is True:  
            idtcA = nivel * '   ' + idtcA + '\n'
            contenido = contenido
            idtcC = nivel * '   ' + idtcC + '\n'
        else:
            idtcA = nivel * '   ' + idtcA
            contenido = contenido
            idtcC = idtcC + '\n'
        if etiqueta == 'br':
            contenido = ''
            idtcC = ''
        return idtcA + contenido + idtcC
    
    def atributos(self,dic):
        '''
        Define los atributos presentes en una etiqueta.
        Recibe como argumento un diccionario donde la llave debe ser el nombre
        del atributo y el valor que debe indicar el valor de ese atributo.
        '''
        listado = ''
        for k,v in dic.items():
            if v != '0':
                atr = ' ' + k + '="' + v + '"'
                listado = listado + atr
        return listado

    def formato(self, etiqueta, contenido):
        '''
        Define el formato para la apertura y cierre de etiquetas.
        Los condicionales if ajustan las particularidades de cada etiqueta.
        Al finalizar el formateo llama a la función self.identación()
        para facilitar la lectura del HTML obtenido.        
        '''
        idtcA = '<' + etiqueta + '>'   # Etiqueta de apertura.
        idtcC = '</' + etiqueta + '>'  # Etiqueta de cierre.
        if etiqueta == 'html':
            idtcA = '<' + etiqueta + """ lang=\"""" + self.lang + """">"""
        if etiqueta == 'meta':
            if contenido == 'charset':
                idtcA = '<' + etiqueta + ' '
                idtcC = """=\"""" + self.charset + """\"/>"""
            elif contenido == 'refresh':
                idtcA = '<' + etiqueta + ' http-equiv="'
                idtcC = '" content="' + self.refresh + """\">"""
            else:
                meta = {'description': self.description,
                        'keywords': self.keywords,
                        'author': self.author,
                        'viewport': self.viewport}
                idtcA = '<' + etiqueta + """ name=\""""
                idtcC = """\" content=\"""" + meta[contenido] + """\"/>"""
        if etiqueta == 'link':
            idtcA = '<' + etiqueta
            idtcC = '/>'
            if contenido == 'stylesheet':
                idtcA = '<' + etiqueta + """ rel=\""""
                idtcC = """" href=\"""" + self.CSS + '"''/>'
        if etiqueta == 'a':
            idtcA = '<' + etiqueta + """ href=\"""" + contenido[0] + """">"""
            contenido = contenido[1]
            idtcC = '</' + etiqueta + '>'
        if etiqueta == 'form':
            idtcA = '<' + etiqueta + self.atributos(self.FormAtr) + '>'
            idtcC = '</' + etiqueta + '>'
        if etiqueta == 'dialog':
            idtcA = '<' + etiqueta + ' open' + '>'
            idtcC = '</' + etiqueta + '>'
        if etiqueta == 'input':
            idtcA = '<' + etiqueta + self.atributos(self.InputAtr) + '>'
            idtcC = ''
#            idtcC = '>'
        if etiqueta == 'address':
            idtcA = '<' + etiqueta + '>'
            contenido = self.formato('a', contenido)
            idtcC = '</' + etiqueta + '>'
        if etiqueta == 'ol':
            idtcA = '<' + etiqueta + ' start="' + self.olStart + '">'
            idtcC = '</' + etiqueta + '>'
        if etiqueta == 'img':
            idtcA = '<' + etiqueta + """ src=\""""
            idtcC = """\">"""
        if etiqueta == 'br' or etiqueta == 'hr':
            idtcC = ''
        if etiqueta == 'source' or etiqueta == 'track':
            idtcC = ''
        return self.identacion(etiqueta, idtcA, contenido, idtcC)
    
    def li(self):
        listado = ''
        for item in self.liList:
            listado = listado + self.formato('li', item)
        return listado


    def Input(self):
        """
        all = autocomplete, autofocus, dirname, disabled, form,
              formnovalidate, list, multiple, name, pattern, placeholder,
              readonly, required, size, type, value
        type = checkbox : checked
        type = date : max, min
        type = file : accept
        type = image: alt, formaction, formenctype, formmethod, formtarget,
                      height, src, width
        type = number : max, maxlength, min, minlength, step
        type = radio : checked
        type = submit: formaction, formenctype, formmethod, formtarget

        type:
            button,
            checkbox,
            color,
            file,
            image,
            radio,
            range,
            reset,
            submit
            ####################
            date,
            datetime-control,
            month,
            time,
            week
            ####################
            email,
            password,
            search,
            text,
            url
            ####################
            number,
            tel,
            ####################
            hidden,
        """
        inputs = ''
        br = self.formato('br','')
        for k,v in self.InputList.items():
            self.InputAtr = v[0]
            etiqueta = self.formato('label',v[2])
            campo = self.formato('input','')
            if v[2] != '':
                inputs = inputs + etiqueta + campo + br + br
            else:
                inputs = inputs + campo
        return inputs


    def TablaCabecera(self):
        '''
        Define el formato para el encabezado de una tabla.
        El atributo TablaEncabezado debe recibir una lista 
        con los nombres de las columnas.
        '''
        fila=''
        for NombreColumna in self.TablaEncabezado:
            fila= fila + self.formato('th', NombreColumna)
        return self.formato('tr', fila)
    
    def TablaCuerpo(self):
        '''
        Define el formato para las filas de una tabla.
        El atributo TablaFilas debe recibir una lista 
        con la lista de los valores de los campos.
        '''
        filas=''
        for fila in self.TablaFilas:
            campos = ''
            for campo in fila:
                campos = campos + self.formato('td', str(campo))
            filas = filas + self.formato('tr', campos)
        return filas

    def TablaPie(self):
        '''
        Define el formato para la fila del pie de una tabla.
        El atributo TablaFilaPie debe recibir una lista 
        con la lista de los valores de los campos.
        '''
        pie=''
        for fila in self.TablaFilaPie:
            campos = ''
            for campo in fila:
                campos = campos + self.formato('td', campo)
            pie = pie + self.formato('tr', campos)
        return pie

    def Tabla(self):
        """Docstring"""
        tabla = (self.formato('table',
            self.formato('caption', self.TablaTitulo) +
            self.formato('thead', self.TablaCabecera()) +
            self.formato('tbody', self.TablaCuerpo())))
        if self.TablaFilaPie == []:
            pass
        else:
            tabla = tabla + self.formato('tfoot', self.TablaPie())
        return tabla


    def Form(self):
        """Docstring"""
        legend = self.formato('legend', self.legendtxt)
        inputs = self.Input()
        fieldset = self.formato('fieldset', legend + inputs)
        self.InputAtr = {'type' : 'submit', 'value' : 'Registrar'}
        br = self.formato('br','')
        submit = br + self.formato('input','')
        formulario = self.formato('form', fieldset + submit)
        return formulario


    def apachepy(self, doctype):
        """Docstring"""
        encabezado = "Content-type:text/html;charset=UTF-8\r\n\r\n"
        return encabezado + "\n" + doctype


    def Doctype(self, html):
        """Docstring"""
        return self.apachepy(self.doctype + "\n" + html)


    def Html(self, funcBody):
        """Docstring"""
        self.head = self.Head()
        self.body = funcBody
        html = self.formato('html', self.head + self.body)
        return self.Doctype(html)


    def Head(self):
        """Docstring"""
        title = self.formato('title', self.title)
        nombres = ['charset', 'refresh', 'description',
                   'keywords', 'author', 'viewport']
        stylesheet = self.formato('link', 'stylesheet')
        meta = ''
        for atributo in nombres:
            meta = meta + self.formato('meta', atributo)
        head = self.formato('head', title + stylesheet + meta)
        return head


    def BodySimple(self):
        """Docstring"""
        self.footer = self.Footer()
        self.article = self.Article()
        self.header = self.Header()
        self.main = self.formato('main', self.article)
        body = self.formato('body', self.header +
                          self.nav +
                          self.aside +
                          self.main +
                          self.footer)
        return body


    def Body6(self):
        """Docstring"""
        self.footer = self.Footer()
        self.article = self.Article()
        self.section = self.Section()
        self.aside = self.Aside()
        self.nav = self.Nav()
        self.header = self.Header()
        self.main = self.formato('main', self.section)
        body = self.formato('body', self.header +
                          self.nav +
                          self.aside +
                          self.main +
                          self.footer)
        return body


    def Body5(self):
        """Docstring"""
        self.footer = self.Footer()
        self.section = self.Section()
        self.aside = self.Aside()
        self.nav = self.Nav()
        self.header = self.Header()
        body = self.formato('body',
                            self.header +
                            self.nav +
                            self.aside +
                            self.section +
                            self.footer)
        return body


    def Body4(self):

        self.footer = self.Footer()
        self.section = self.Section()
        self.nav = self.Nav()
        self.header = self.Header()
        body = self.formato('body',
                            self.header +
                            self.nav +
                            self.section +
                            self.footer)
        return body


    def Body3(self):
        """Docstring"""
        self.footer = self.Footer()
        self.section = self.Section()
        self.header = self.Header()
        body = self.formato('body',
                            self.header +
                            self.section +
                            self.footer)
        return body


    def Body2(self):
        """Docstring"""
        self.section = self.Section()
        self.header = self.Header()
        body = self.formato('body',
                            self.header +
                            self.section)
        return body


    def Body1(self):
        """Docstring"""
        self.section = self.Section()
        body = self.formato('body',
                            self.section)
        return body


    def Header(self):
        """Docstring"""
        h1 = self.formato('h1', self.h1)
        return self.formato('header', h1)


    def Nav(self):
        """Docstring"""
        h2 = self.formato('h2', self.h2)
        return self.formato('nav', h2)


    def Aside(self):
        """Docstring"""
        h3 = self.formato('h3', self.h3)
        return self.formato('aside', h3)


    def Section(self):
        """Docstring"""
        h4 = self.formato('h4', self.h4)
        return self.formato('section', h4 + self.Form() + self.article)


    def Article(self):
        """Docstring"""
        h5 = self.formato('h5', self.h5)
        return self.formato('article', h5 + self.Tabla())


    def Footer(self):
        """Docstring"""
        figcaption = self.formato('figcaption', self.gpl3[1])
        img = self.formato('img', self.gpl3[0])
        figure = self.formato('figure', img + figcaption)
        h6 = self.formato('h6', self.h6)
        return self.formato('footer', h6 + figure)


    def exportar(self):
        '''
        Función para exportar el html generado a un archivo.
        '''
        try:
            import sys
            sys.stdout = open(self.htmlpath + self.htmlFile + self.htmlext, 'w')
            print(self.plantilla())
            sys.stdout.close()
        except FileNotFoundError:
            import os
            if not os.path.exists(self.htmlpath):
                os.makedirs(self.htmlpath)
            cfg = open(self.htmlpath + self.htmlFile + self.htmlext, "w")
            cfg.write(os.linesep)
            cfg.close()
            self.exportar()

# Programa principal
            
try:
    if __name__ == '__main__':
        try:
            from configApp import eventos
            log=eventos('html5')
            log.debug('html5.py ejecutado')
        except:
            import sys
            import logging
            logging.basicConfig(filename='logs/html5.log', level=logging.ERROR,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error('Error de ejecucion')
            logging.error(sys.exc_info())
    else:
        pass
### Devuelve error ###
#        from .__init__ import eventos
#        log=eventos('html5')
#        log.debug('html5.py importado')
except ImportError:
    print('error al importar html5.py')
 