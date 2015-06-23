# BillApp
Models
Si se va a probar desde Windows 10, recomiendo instalar ActivePython-3.4.1.0-win64-x64 (Abajo Enlace), para evitar problemas.
https://www.dropbox.com/s/nzp9nqg19oslbtr/ActivePython-3.4.1.0-win64-x64.msi?dl=0

Crear el Entorno Virtual vwrok
  python -m venv vwork
Activar el Entorno Virtual
  vwork\Scripst\activate
Instalar Django
  pip install django
Instalar el conector de MySQL
  pip install mysqlclient
Instalar Django REST Framework
  pip install django djangorestframework
Instalar Django Suit
  pip install django-suit
  
Comandos Django:
Para obtener una lista de ´instrucciones django´ use el comando:
  django-admin ––help
Comandos mas usados:
  python manage.py startproject: crea un nuevo proyecto.
  python manage.py startapp: crea una nueva aplicación.
  python manage.py runserver: inicia el servidor.
  python manage.py syncdb: sincroniza el modelo con la base de datos.
  python manage.py makemigrations: Prepara los modelos para reflejarlos en la base de datos.
  python manage.py migrate: Refleja los modelos en la base de datos.
  python manage.py createsuperuser: Crea un super usuario para el administrador.
  
Configurar el Settings.py para la BD
BASE DE DATOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'user_id',
        'PASSWORD': 'user_password',
        'HOST': 'host',
        'PORT': 'port',
    }
}


Hacer las Pruebas!!!!
(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)(´･_･`)
