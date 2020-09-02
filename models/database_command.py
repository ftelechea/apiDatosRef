# -*- coding: utf-8 -*-
"""Class DatabaseCommand

Esta clase permite realizar la conexión a una base de datos PostgreSQL
Cuenta con métodos para obtener un conjunto de datos (diccionario serializado) o un escalar (único valor).

Example:
    Para crear una instancia de la clase:
            my_data_access = database_command.DatabaseCommand()
    Para invocar un método de la clase:
            result = my_data_access.execute_sql_dataset(strSelect)


Attributes:
    variables privadas de la clase (str):    __server,  __database __username __password }
    Estas variables se cargan a partir de un archivo JSON configTrzDB.json
Todo:
    * 
    * 

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from flask_jsonpify import jsonify
import psycopg2 #módulo para conectarse a PostgreSQL
import psycopg2.extras #para retornar resultado de consulta como diccionario
import json

class DatabaseCommand:

    def __init__(self):

        #Leer datos de conexión a la base desde el archivo configDB.json
        with open('models/configDB.json') as json_data_file:
            database_config = json.load(json_data_file)["postgresql"]
        
        #Variables Privadas de la Clase
        self.__server = database_config["server"]        
        self.__database = database_config["database"]
        self.__username = database_config["username"]
        self.__password = database_config["password"]

    def execute_sql_dataset(self, sqlStatemant):
        
        #crear conexión a la base
        connDB = psycopg2.connect(database=self.__database, host=self.__server, user=self.__username, password=self.__password)
        
        cursor = connDB.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        #ejecutar sentencia sql
        cursor.execute(sqlStatemant)

        my_dictionary = cursor.fetchall()

        #cerrar los objetos de base de datos abiertos
        cursor.close
        connDB.close()

        return jsonify(my_dictionary)

