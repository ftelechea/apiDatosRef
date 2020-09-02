from flask import Flask, request
from flask_restful import Api
from flasgger import Swagger, swag_from

#importación de las clases que modelan los recursos
from models.model import Paises, Departamentos, Sexos
from models.model import Generos, EstadosCiviles, TiposDocumentosPersona

app = Flask(__name__)
api = Api(app)

# Create an APISpec
template = {
  "swagger": "2.0",
  "info": {
    "title": "Datos referenciales (codigueras)",
    "description": "En el marco de la definición de la arquitectura integrada de gobierno se definen conjuntos de datos referenciales sobre entidades comunes del Estado. Estos conjuntos de datos forman parte de la Arquitectura de Datos de Gobierno y definen los valores posibles para algunos dominios de datos generales, que permiten la integración y comunicación entre los organismos del Estado. Cada conjunto de datos definido representa un dominio específico y está representado como una lista codificada.",
    "version": "0.1",
    "contact": {
      "name": "Agesic",
      "url": "https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/",
    }
  },
}

app.config['SWAGGER'] = {
    'title': 'API - Datos Referenciales',
    'uiversion': 2,
    "specs_route": "//catalogodatos/referenciales/"
}

swag = Swagger(app, template= template)

api.add_resource(Paises, '/catalogodatos/referenciales/paises') 
api.add_resource(Departamentos, '/catalogodatos/referenciales/departamentos') 
api.add_resource(Sexos, '/catalogodatos/referenciales/sexos') 
api.add_resource(Generos, '/catalogodatos/referenciales/generos') 
api.add_resource(EstadosCiviles, '/catalogodatos/referenciales/estadosciviles') 
api.add_resource(TiposDocumentosPersona, '/catalogodatos/referenciales/tiposdocumentospersona')

#No se necesita si se utiliza Gunicorn para ejecutar la app
""" if __name__ == '__main__':
     app.run(port='5002')
 """