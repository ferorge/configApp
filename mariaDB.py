#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from MySQLdb import connect
from MySQLdb import Error

class SQL():
    def __init__(self):
        self.pathcfg   = ''
        self.host      = ''
        self.port      = 0
        self.database  = ''
        self.user      = ''
        self.password  = ''
        self.servidor  = False
        self.bd        = ''
        self.puntero   = False
        self.PA        = 'Procedimiento almacenado'
        self.parametros= []
        self.tabla = ''
        self.nombre = ''
        self.ProcAlm = ''
        self.info = None
        self.error = None
        self.sentencia = ''
        self.sentenciaFiltro = None
        self.cabecera  = []
        self.filas     = []
        self.totales   = []
    def VerificarConexion(self):
        import os.path
        if os.path.isfile(self.pathcfg):
            from configparser import ConfigParser
            srv = ConfigParser()
            srv.read(self.pathcfg)
            try:
                if srv.get("Servidor","config") is None:
                    self.CrearConexion()
                elif srv.get("Servidor","config") == 'true':
                    self.host     = srv['Servidor']['host']
                    self.port     = int(srv['Servidor']['port'])
                    self.database = srv['Servidor']['database']
                    self.user     = srv['Servidor']['user']
                    self.password = srv['Servidor']['password']
                else:
                    print(srv.get("Servidor","config"))
                    self.CrearConexion()
            except:
                self.CrearConexion()
        else:
            cfg = open(self.pathcfg, "w")
            cfg.write(os.linesep)
            cfg.close()
            self.VerificarConexion()
    def CrearConexion(self):
        from configparser import ConfigParser
        srv = ConfigParser()
        srv.read(self.pathcfg)
        srv.remove_section("Servidor")
        srv.add_section("Servidor")
        srv.set("Servidor", "host",
                input("Indique la dirección del servidor mariadb: "))
        srv.set("Servidor", "port",
                input("Indique el puerto del servidor mariadb: "))
        srv.set("Servidor", "database",
                input("Indique la base de datos de la aplicación: "))
        srv.set("Servidor", "user",
                input("Indique el usuario de la aplicación: "))
        srv.set("Servidor", "password",
                input("Indique la contraseña: "))
        srv.set("Servidor", "config", "true")
        with open(self.pathcfg, "w") as f:
            srv.write(f)
        self.VerificarConexion()
    def AbrirConexion(self):
        try:
            '''Apertura de conexión a base de datos'''
            self.servidor = connect(charset='utf8',
                                    init_command='SET NAMES UTF8',
                                    # Nombre de servidor
                                    host=self.host,
                                    # Puerto de servidor
                                    port=self.port,
                                    # Usuario de mariaDB
                                    user=self.user,
                                    # Contraseña de usuario
                                    passwd=self.password,
                                    # Nombre de BD
                                    db=self.database)
#            logging.debug("Conexión abierta")
            return self.servidor
        except Error as error:
            self.VerificarConexion()
            self.error = str(error)
    def AbrirPuntero(self, servidor):
        try:
            self.puntero = servidor.cursor()
#            logging.debug("Puntero abierto")
            return self.puntero
        except Error as error:
            self.error = str(error)
    def CerrarPuntero(self, puntero):
        try:
            puntero.close()
#            logging.debug("Puntero cerrado")
        except Error as error:
            self.error = str(error)
    def CerrarConexion(self, servidor):
        try:
            servidor.close()
#            logging.debug("Conexión cerrada")
        except Error as error:
            self.error = str(error)
    def LlamarPA(self, servidor, puntero, pa, parametros):
        try:
            # Llamado a procedimiento almacenado
            puntero.callproc(pa,parametros)
            # Confirmación de transacción
            servidor.commit()
            self.info = "Transacción realizada: " + pa
        except Error as error:
            servidor.rollback()
            self.error = str(error)


    def Consultar(self):
        """Realiza la consulta del atributo self.sentencia a la base de datos.
        Agrega los títulos de la tabla al atributo self.cabecera y los 
        valores de las filas al atributo self.filas.
        Utilizar el atributo self.sentenciaFiltro para fijar algún filtro."""
        self.bd=self.AbrirConexion()
        cursor=self.AbrirPuntero(self.bd)
        if self.sentenciaFiltro is None:
            cursor.execute(self.sentencia)
        else:
            cursor.execute(self.sentencia, (self.sentenciaFiltro,))
        if cursor.description is None:
            print('No hay datos para mostrar.')
        else:
            self.cabecera = [i[0] for i in cursor.description]
        tabla = cursor.fetchall()
        if tabla is None:
            print('No hay datos para mostrar.')
        else:
            for fila in tabla:
                DatoFila = []
                for campo in fila:
                     DatoFila.append(str(campo))
    #                if type(campo) is Decimal:
    #                    DatoFila.append(float(campo))
    #                else:
    #                    DatoFila.append(str(campo))
                self.filas.append(DatoFila)
        self.CerrarPuntero(cursor)
        self.CerrarConexion(self.bd)


    def Registrar(self):
        '''Llama al procedimiento almacenado (PA) de mariaDB 
        pasando como argumento el nombre del PA y sus parámetros de entrada.'''
#        logging.basicConfig(filename=EventosFichero,
#                            level=logging.DEBUG,
#                            format='%(asctime)s - %(name)s - \
#                            %(levelname)s - %(message)s')
        self.bd = self.AbrirConexion()
        cursor = self.AbrirPuntero(self.bd)
        self.LlamarPA(self.bd, cursor, self.PA, self.parametros)
        self.CerrarPuntero(cursor)
        self.CerrarConexion(self.bd)


    def DicReq(self,API,key):
        '''Devuelve un diccionario de la API de un sitio.'''
        try:
#        logging.basicConfig(filename=EventosFichero,
#                            level=logging.DEBUG,
#                            format='%(asctime)s - %(name)s - \
#                            %(levelname)s - %(message)s')
            import requests
            sesion = requests.Session()
            if key is None:
                pass
            else:
                headers = {
                    'Accepts': 'application/json',
                    'X-CMC_PRO_API_KEY': key,
                }
                sesion.headers.update(headers)
            respuesta = sesion.get(API)
            import json
            sitio = json.loads(respuesta.text)
#            logging.debug('DicReq OK. El fichero sitio fue obtenido.')
            return sitio
        except:
            pass
#            logging.exception("DicReq error.\
#                               Error al obtener el fichero del sitio.")


    def DicReg(self,PA,diccionario):
        '''Registra el diccionario obtenido como argumento en la base de datos,
        llamando al procedimiento almacenado obtenido como argumento.'''
        try:
            conexion=SQL()
            conexion.VerificarConexion()
            conexion.PA = PA
            for valores in diccionario.values():
                conexion.parametros = valores
                conexion.Registrar()
#            logging.info("DicReg OK.")
        except:
            pass
#            logging.exception("DicReg error.")


    def ObtenerParametros(self, tabla):
        self.sentencia = "SELECT campo, posicion, label,\
        autocomplete, autofocus, dirname, disabled,\
        form, formnovalidate, list, multiple, name, pattern, placeholder,\
        readonly, required, size, type, value \
        FROM 0040_Campos \
        WHERE id_tabla = %s ORDER BY posicion;"
        self.sentenciaFiltro = tabla
        self.VerificarConexion()
        self.Consultar()
        campos = {}
        for fila in self.filas:
            n = 2
            parametros = {}
            for valor in fila[3:20]:
                n = n + 1
                parametros[self.cabecera[n]] = valor
#            print(fila[0], fila[1], fila[2], parametros, end='\n', sep='\n')
            campos[fila[0]] = (parametros, fila[1], fila[2])
#        print(campos)
        return campos


    def RegistrarCampos(self, objCREAR):
        """Registra los campos de los formularios de la aplicación.
        Debe recibir como parametro una instancia de la clase CREAR()."""
        self.PA = 'CAMC'
        i = objCREAR
        for k, v in i.campos.items():
            self.parametros = [v[0]['PA'],
                             k,
                             v[0]['CampoActivo'],
                             v[0]['id_tabla'],
                             v[0]['AyudaUsuario'],
                             v[0]['tipo'],
                             v[0]['tamaño'],
                             v[0]['comentario'],
                             v[0]['default'],
                             v[0]['nulo'],
                             v[0]['signo'],
                             v[0]['pk'],
                             v[0]['uk'],
                             v[0]['fk'],
                             v[1]['posicion'],
                             v[1]['label'],
                             v[2]['autocomplete'],
                             v[2]['autofocus'],
                             v[2]['dirname'],
                             v[2]['disabled'],
                             v[2]['form'],
                             v[2]['formnovalidate'],
                             v[2]['list'],
                             v[2]['multiple'],
                             (3 - len(str(v[1]['posicion']))) * '0' +
                             str(v[1]['posicion']) + '_' + v[2]['name'],
                             v[2]['pattern'],
                             v[2]['placeholder'],
                             v[2]['readonly'],
                             v[2]['required'],
                             v[2]['size'],
                             v[2]['type'],
                             v[2]['value']]
            self.Registrar()
            if self.info != None:
                print('info: ', self.info)
            if self.error != None:
                print('error: ', self.error)


class CREAR():
    """Docstring"""
    def __init__(self):
        self.NumeroTabla = 0
        self.NombreTabla = 'Por favor defina el nombre de la tabla.'
        self.campo = 'nombre'
        self.campoPosicion = 0
        self.campos = {}
        self.dicSQL = {}
        self.dicFIELD = {}
        self.dicHTML = {}
        self.defSQL = {'PA': None,
                       'CampoActivo': True,
                       'id_tabla': None,
                       'AyudaUsuario': None,
                       'tipo': None,
                       'tamaño': None,
                       'comentario': None,
                       'default': None,
                       'nulo': True,
                       'signo': None,
                       'pk': False,
                       'uk': False,
                       'fk': False}
        self.defFIELD = {'posicion': None,
                         'label': None}
        self.defHTML = {'autocomplete': True,
                        'autofocus': False,
                        'dirname': False,
                        'disabled': False,
                        'form': False,
                        'formnovalidate': False,
                        'list': False,
                        'multiple': False,
                        'name': False,
                        'pattern': False,
                        'placeholder': False,
                        'readonly': False,
                        'required': True,
                        'size': False,
                        'type': 'text',
                        'value': False}
        self.ComentarioTabla = 'Por favor defina el comentario de la tabla.'
        self.engine = 'ENGINE=InnoDB'
        self.charset = 'DEFAULT CHARSET=utf8mb4'
        self.NombreVista = 'Por favor defina el nombre de la vista.'
        self.NombrePA = 'Por favor defina el nombre del proc. almacenado.'
        self.ComentarioPA = 'Por favor defina el comentario del proc. alm.'


    def CamposHTML5(self):
        """Docstring"""
        campos = {}
        etiqueta = ''
        atributos = {}
#        i = SQL()
        self.sentencia = "SELECT autocomplete, autofocus, dirname, disabled,\
                       form, formnovalidate, list, multiple, name, pattern,\
                       placeholder, readonly, required, size, type, value\
                       FROM 0040_Campos WHERE campo = 'PAR';"
        print(self.Consultar())
        for k,v in self.campos.items():
            etiqueta = v[1]['label']
            atributos = v[2]
            campos[k] = (atributos, etiqueta)
        return campos


    def CamposTabla(self):
        campos = ''
        # pk = ''
        pk = []
        uk = []
        fk = []
        for k,v in self.campos.items():
            nombre = '`' + k + '`' + ' '
            tipo = v[0]['tipo'] + ' '
            if v[0]['tamaño'] is None:
                tamaño = ''
            else:
                tamaño = '(' + v[0]['tamaño'] + ')'+ ' '
            cmt = "COMMENT '" + v[0]['comentario'] + "',"
            if v[0]['default'] is None:
                default = ''
            else:
                default = 'DEFAULT ' + v[0]['default'] + ' '
            if v[0]['nulo'] is True:
                nulo = 'NULL' + ' '
            else:
                nulo = 'NOT NULL' + ' '
            signo = ''
            if v[0]['signo'] is True:
                signo = 'SIGNED' + ' '
            elif v[0]['signo'] is False:
                signo = 'UNSIGNED' + ' '
            else:
                signo = ''
            if v[0]['pk'] is True:
                # pk = nombre
                pk.append(nombre)
            if v[0]['uk'] is True:
                uk.append(nombre)
            if v[0]['fk'] != False:
                fk.append(v[0]['fk'])
            campos = campos + nombre + tipo + tamaño + signo + default + \
            nulo + cmt + "\n"
        return campos, pk, uk, fk


    def CamposVista(self):
        """Docstring"""
        campos = ''
        for k,v in self.campos.items():
            nombre = '`' + k + '`' + ' '
            campos = campos + nombre + " AS '" + v[1]['label'] + "'," + "\n"
        campos = campos[:len(campos)-2] + "\n"
        return campos


    def CamposPA(self):
        campos1 = ''
        campos2 = ''
        for k,v in self.campos.items():
            nombre = '`p_' + k + '`'
            tipo = ' ' + v[0]['tipo'] + ' '
#            tamaño = '(' + v[0]['tamaño'] + ')'+ ','
            if v[0]['tamaño'] is None:
                tamaño = ''
            else:
                tamaño = '(' + v[0]['tamaño'] + ')'+ ' '
            campos1 = campos1 + nombre + tipo + tamaño + ',' + "\n"
            campos2 = campos2 + nombre + ',' + "\n"
        campos1 = '(' + "\n" + campos1[:len(campos1)-2] + ')' + "\n"
        campos2 = '(' + "\n" + campos2[:len(campos2)-2] + ')' + ';' + "\n"
        return (campos1, campos2)


    def SentenciaCrearTabla(self):
        """Docstring"""
        ct = 'CREATE TABLE IF NOT EXISTS '
        # nombre = '`' + self.NombreTabla + '`'
        nombre = '`' + self.NumeroTabla + '_' + self.NombreTabla + '`'
        comentario = "COMMENT='" + self.ComentarioTabla + "'"
        campos = self.CamposTabla()
        pk = ''
        for k in campos[1]:
            pk = pk + k + ', '
        cpk = 'CONSTRAINT pk_' + self.NumeroTabla + '_' + self.NombreTabla + \
              ' PRIMARY KEY (' + pk[:len(pk)-2] + ')'
        cuk = ''
        if len(campos[2]) > 0:
            nuk = 0
            for uk in campos[2]:
                nuk = nuk + 1
                cuk = cuk + ',' + "\n" +'CONSTRAINT uk_' + \
                self.NombreTabla + str(nuk) + \
              ' UNIQUE KEY (' + uk + ')'
        else:
            cuk= ''
        cfk = '' # Constraint Foreign Key
        if len(campos[3]) > 0:
            nfk = 0
            for fk in campos[3]:
                nfk = nfk + 1
                cfk = cfk + ',' + "\n" +'CONSTRAINT fk_' + \
                self.NombreTabla + str(nfk) + \
              ' FOREIGN KEY (' + fk + ')'+ \
              ' REFERENCES' + \
              ' ON DELETE RESTRICT ON UPDATE CASCADE'
        else:
            cfk= ''
        return (ct + nombre + ' ('  + "\n" +
                campos[0] +
                cpk +
                cuk + "\n" +
                ')' + "\n" +
                comentario + "\n" +
                self.engine + "\n" +
                self.charset + ';')


    def SentenciaCrearVista(self):
        """Docstring"""
        cv = 'CREATE OR REPLACE VIEW '
        # nombre = '`' + self.NombreVista + '`'
        # tabla = '`' + self.NombreTabla + '`'
        nombre = '`' + self.NombreVista + self.NumeroTabla + '`'
        tabla = '`' + self.NumeroTabla + '_' + self.NombreTabla + '`'
        campos = self.CamposVista()
        return (cv + nombre + ' AS SELECT'  + "\n" + 
                campos + 
                'FROM ' + tabla + ';')


    def SentenciaCrearPA(self):
        cpa = 'CREATE OR REPLACE PROCEDURE '
        nombre = '`' + self.NombrePA + '`'
        campos = self.CamposPA()
        comentario = "COMMENT '" + self.ComentarioPA + "'" + "\n"
        acciones = 'INSERT INTO ' + self.NumeroTabla + '_' + \
                   self.NombreTabla + ' VALUES ' + campos[1]
        BeginEnd = 'BEGIN' + "\n" + acciones + 'END ;' + "\n"
#        delimiter = 'DELIMITER //' + "\n" + cpa + nombre + campos[0] + \
#                    comentario + BeginEnd + 'DELIMITER ;'
#        return delimiter
        return str(cpa + nombre + campos[0] + \
               comentario + BeginEnd)


    def CrearTabla(self,insSQL):
        """Docstring"""
        insSQL.sentencia = self.SentenciaCrearTabla()
        insSQL.Consultar()


    def CrearVista(self, insSQL):
        """Docstring"""
        insSQL.sentencia = self.SentenciaCrearVista()
        insSQL.Consultar()


    def CrearPA(self, insSQL):
        """Docstring"""
        insSQL.sentencia = self.SentenciaCrearPA()
        insSQL.Consultar()


    def reset(self, insSQL):
        """Docstring"""
        insSQL.sentencia = 'DROP TABLE IF EXISTS ' + \
        self.NumeroTabla + '_' + self.NombreTabla
        insSQL.Consultar()
        self.CrearTabla(insSQL)
        insSQL.sentencia = 'DROP VIEW IF EXISTS ' + \
        self.NombreVista + self.NumeroTabla
        insSQL.Consultar()
        self.CrearVista(insSQL)
        insSQL.sentencia = 'DROP PROCEDURE IF EXISTS ' + self.NombrePA
        insSQL.Consultar()
        self.CrearPA(insSQL)


    def CrearCampo(self, **kwargs):
        """Docstring"""
        lista01 = ['PA', 'CampoActivo', 'id_tabla', 'AyudaUsuario', 'tipo',
                   'tamaño', 'comentario', 'default', 'nulo', 'signo', 'pk',
                   'uk', 'fk']
        lista02 = ['posicion', 'label']
        lista03 = ['autocomplete', 'autofocus', 'dirname', 'disabled', 'form',
                   'formnovalidate','list', 'multiple', 'name', 'pattern',
                   'placeholder', 'readonly', 'required', 'size', 'type',
                   'value']
        self.dicSQL = self.defSQL.copy()
        self.dicFIELD = self.defFIELD.copy()
        self.dicHTML = self.defHTML.copy()
        for kw in kwargs:
#            print(kw)
            for arg in lista01:
                if kw == arg:
                    self.dicSQL[kw] = kwargs[kw]
                else:
                    for arg in lista02:
                        if kw == arg:
                            self.dicFIELD[kw] = kwargs[kw]
                        else:
                            for arg in lista03:
                                if kw == arg:
                                    self.dicHTML[kw] = kwargs[kw]
                                else:
                                    pass
#                                    print(arg, ' no es un valor esperado.')
        self.dicFIELD['posicion'] = self.campoPosicion
        self.campos[self.campo] = [self.dicSQL, self.dicFIELD, self.dicHTML]
        self.campoPosicion=self.campoPosicion + 10
#        print(self.campos)



#    def ParsPorPA(self,parametro):
#        self.sentencia = self.algo
#        tipo=list(sum(self.Consulta(parametro), ()))
#        return tipo
#    def InsPars(self):
#        '''Imprime en STDOUT las llamadas al procedimiento almacenado PARC para agregar los parámetros de nuevos PA a la tabla de parámetros.'''
#        #sys.stdout = open('../sql/07.CuidAr.Parametros.sql', 'w')
#        self.sentencia="SELECT 'PARC','AdminCuidAr',Procedimiento,Orden,True, False, False, DatoHTML, Parámetro, Etiqueta, Input,'' FROM `InfSchPar`;"
#        for registro in self.Consulta(None):
#            print('CALL PARC', registro,';')
#        self.sentencia = "SELECT 'PARC','AdminCuidAr', idPA, '0', True, True,False, 'hidden', 'PA', 'PA', 'PA', 'Indique el nombre del PA.'  FROM 0070_Transacciones GROUP BY idPA;"
#        for registro in self.Consulta(None):
#            print('CALL PARC', registro,';')

# Programa principal
            
try:
    if __name__ == '__main__':
        import sys
        sys.path.append('./')
        try:
            from configApp import eventos
            log=eventos('mariaDB')
            log.debug('mariaDB.py ejecutado')
            SQL.Registrar()
        except:
            import logging
            logging.basicConfig(filename='logs/mariaDB.log', level=logging.ERROR,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error('Error de ejecucion')
            logging.error(sys.exc_info())
    else:
        pass
### Devuelve error ###
#        from .__init__ import eventos
#        log=eventos('mariaDB')
#        log.directorio = '../logs/'
#        log.config()
#        log.debug('mariaDB.py importado')
except ImportError:
    print('error al importar mariaDB.py')



#        self.idModulosActivos       = "SELECT idModulo FROM 0050_Modulos WHERE ModuloActivo = TRUE ORDER BY idModulo;"
#        self.ModulosActivos         = "SELECT idModulo, modulo FROM 0050_Modulos WHERE ModuloActivo = TRUE ORDER BY idModulo;"
#        self.TransaccionesPorModulo = "SELECT idTransaccion, idPA, negocio, id_modulo  FROM 0070_Transacciones WHERE TransaccionActiva = TRUE;"
#        self.TransaccionesDelModulo = "SELECT idTransaccion, transaccion, negocio FROM 0070_Transacciones WHERE TransaccionActiva = TRUE AND id_modulo = %s;"
#        self.Inputs                 = "SELECT `HTMLId`,`HTMLType`,`HTMLLabel`,`HTMLplaceholder`,`HTMLrequired`,`HTMLhidden` FROM 0080_Parametros WHERE id_procedimiento = %s;"
#        self.algo                   = "SELECT DatoHTML,Input FROM InfSchPar WHERE Input = %s GROUP BY DatoHTML;"
 