# DESPLEGAR APLICACION FLASK CON GUNICORN & NGINX 
Paso a paso para:
* Crear entorno virtual e instalar paquetes a partir de requirements.txt
* Configurar Gunicorn como application server
* Configurar Nginx como un front-end reverse proxy.

### Crear entorno virtual e instalar paquetes

Realizar los siguientes pasos:
* Copiar o clonar de github (este repositorio) archivos de la aplicación.
* Crear entorno virtual Python e instalar paquetes con los siguientes comandos:

```
cd apiDatosRef
sudo python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configurar servicio Gunicorn 

Crear archivo .service (utilizando el editor de su preferencia, en este caso nano), en directorio /etc/systemd/system para configurar servicio de Gunicorn para las peticiones de la API:
* sudo nano /etc/systemd/system/api_datosref.service
* ingresar el siguiente contenido en el archivo:

```
[Unit]
Description=Instancia Gunicorn para atender peticiones de la API de Datos Referenciales
After=network.target

[Service]
User=root
Group=adm
WorkingDirectory=/opt/apiDatosRef/
Environment="PATH=/opt/apiDatosRef/venv/bin/"
ExecStart=/opt/apiDatosRef/venv/bin/gunicorn --workers 2 --bind unix:api_datosref.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

### Configurar NGINX

Después de instalar nginx, se configura de la siguiente forma:
* sudo nano /etc/nginx/sites-available/api_datosref
* Ingresar el siguiente contenido en el archivo:

```
server {
    listen 8000;
    server_name 127.0.0.1;

    location / {
        include proxy_params;
        proxy_pass http://unix:/opt/apiDatosRef/api_datosref.sock;
    }
}
```



* Crear symlink hacia sites-enabled con el comando: 
sudo ln -s /etc/nginx/sites-available/api_datosref /etc/nginx/sites-enabled

**NOTA: revisar en archivo de configuración de nginx el usuario seteado** con sudo nano /etc/nginx/nginx.conf

* Chequear sintaxis de NGINX con el comando:
sudo nginx -t

* Reiniciar el servicio de NGINX con el comando:
sudo service nginx restart
