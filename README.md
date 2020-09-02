# API Rest para datos referenciales (codigueras)
Se utiliza Flask y la extensión flask_restful para implementar la API. Se accede a una base PostgreSQL, donde se encuentran las tablas codigueras para:
* Paises
* Departamentos
* Tipos de Documentos de Persona
* Estados Civiles
* Sexos
* Géneros

El acceso a la base de datos, se realiza directamente a través del controlador psycopg2 (no se utiliza ORM). La clase DatabaseCommand implementada en database_command.py (directorio models), realiza la conexión a la base, gestiona los objetos connection y cursor, permitiendo la ejecución de consultas SQL, devolviendo un JSON a través de jsonify (módulo flask_jsonpify).

En el archivo "step_by_step_Deploy.txt", se especifican los pasos para:
* Generar un entorno virtual Python e instalar todos los paquetes necesarios a través del archivo requirements.txt.
* Desplegar la API con Gunicorn WSGI como servidor de aplicación y NGINX actuando como front-end reverse proxy.


