from flask_restful import Resource
import models.database_command as db

class Paises(Resource):

    def get(self):
        """
        Retorna la lista de Países
        Codificación de países de acuerdo a la norma ISO 3166-1:2007
        ---
        tags:
          - paises
        responses:
          200:
            description: lista de países
            schema:
              id: Paises
              properties:
                cod_pais:
                  type: string
                  description: Código de País
                cod_alfa_2: 
                  type: string
                  description: Código alfanumérico de 2 caracteres
                cod_alfa_3: 
                  type: string
                  description: Código alfanumérico de 3 caracteres                  
                nombre_pais:
                  type: string
                  description: Nombre de País
        """
        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
            		
        select_Query = ("select "
	                    "cod_pais, "
                        "cod_alfa_2, "
                        "cod_alfa_3, "
                        "nombre_pais "
                        "from dat_referenciales.cod_paises "
                        "order by nombre_pais")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result

class Departamentos(Resource):

    def get(self):
        """
        Retorna la lista de Departamentos
        Codificación de acuerdo a la norma ISO 3166-2:2007
        ---
        tags:
          - departamentos
        responses:
          200:
            description: lista de departamentos
            schema:
              id: Departamentos
              properties:
                cod_departamento:
                  type: string
                  description: Código de Departamanto
                nombre_departamento:
                  type: string
                  description: Nombre de Departamanto
        """
        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
        		
        select_Query = ("select "
	                    "cod_departamento, "
                        "nombre_departamento "
                        "from dat_referenciales.cod_departamentos "
                        "order by nombre_departamento")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result

class Sexos(Resource):

    def get(self):
        """
        Retorna la lista de Sexos
        Codificación del sexo entendido como “el conjunto de características biológicas que definen al espectro de humanos como hembras y machos" (Organización Mundial de la Salud).
        ---
        tags:
          - sexos
        responses:
          200:
            description: lista de sexos
            schema:
              id: Sexos
              properties:
                cod_sexo:
                  type: integer
                  description: Código de Sexo
                nombre_sexo:
                  type: string
                  description: Nombre de Sexo
                descripcion_sexo:
                  type: string
                  description: Descripción de Sexo
        """

        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
        		
        select_Query = ("select "
	                    "cod_sexo, "
                        "nombre_sexo, "
                        "descripcion_sexo "
                        "from dat_referenciales.cod_sexos "
                        "order by cod_sexo")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result

class Generos(Resource):

    def get(self):
        """
        Retorna la lista de Géneros
        Codificación del género entendido como la construcción cultural referida a la diferencia sexual de los individuos de la especie humana
        ---
        tags:
          - géneros
        responses:
          200:
            description: lista de géneros
            schema:
              id: Generos
              properties:
                cod_genero:
                  type: integer
                  description: Código de Género
                nombre_genero:
                  type: string
                  description: Nombre de Género
                descripcion_genero:
                  type: string
                  description: Descripción de Género
        """

        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
        		
        select_Query = ("select "
	                    "cod_genero, "
                        "nombre_genero, "
                        "descripcion_genero "
                        "from dat_referenciales.cod_generos "
                        "order by cod_genero")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result  

class EstadosCiviles(Resource):

    def get(self):
        """
        Retorna la lista de Estados Civiles
        Codificación del estado civil entendido como la situación de las personas determinada por sus relaciones de familia, provenientes del matrimonio, que establece ciertos derechos y deberes
        ---
        tags:
          - estados civiles
        responses:
          200:
            description: lista de estados civiles
            schema:
              id: EstadosCiviles
              properties:
                cod_estado_civil:
                  type: string
                  description: Código de Estado Civil
                nombre_estado_civil:
                  type: string
                  description: Nombre de Estado Civil
                descripcion_estado_civil:
                  type: string
                  description: Descripción de Estado Civil
        """
        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
        		
        select_Query = ("select "
	                    "cod_estado_civil, "
                        "nombre_estado_civil, "
                        "descripcion_estado_civil "
                        "from dat_referenciales.cod_estados_civiles "
                        "order by nombre_estado_civil")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result

class TiposDocumentosPersona(Resource):

    def get(self):
        """
        Retorna la lista de Tipos de Documentos que identifican Personas
        Codificación según adaptación de la UNAOID para el estándar ICAO
        ---        
        tags:
          - tipos documentos persona
        responses:
          200:
            description: lista de tipos de documento
            schema:
              id: TiposDocumentosPersona
              properties:
                cod_tipo_documento:
                  type: integer
                  description: Código de Tipo de Documento
                descripcion_tipo_documento:
                  type: string
                  description: Descripción del Tipo de Documento
        """

        #crear conexión a la base
        my_data_access = db.DatabaseCommand()
        		
        select_Query = ("select "
	                    "cod_tipo_documento, "
                        "descripcion_tipo_documento "
                        "from dat_referenciales.cod_tipos_documentos "
                        "order by cod_tipo_documento")
	
        #ejecutar sentencia sql
        result = my_data_access.execute_sql_dataset(select_Query)
        return result