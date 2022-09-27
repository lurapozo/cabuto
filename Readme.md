# Cabutos Backend
Web Site administrador Cabuto Market

## Sobre el proyecto
Rest Api Cabuto es un proyecto que se encarga de la administración, funcionalidad, seguridad y optimización de recursos de la empresa Minimarket Cabutos.

## Tecnologías

Repositorio de pruebas para el proyecto deCabuto. Esta desarrollador totalmente en Django framework de Python 3.8.10 . Conecta a una base de datos relacional en MySQL.

Se encuentra desplegado en [PythonAnywhere](https://www.pythonanywhere.com/)

## Requisitos

Se recomienda usar Ubuntu 20.04

Y tener instalado MySQL y PostgreSQL server

## Instalación

Clonar el proyecto
```
git clone https://github.com/lurapozo/cabuto.git
```

Crear un entorno virtual para que las dependencias instaladas y sus versiones se manejen dentro del contexto del proyecto y no de forma global.

```
python -m venv myvenv
```
Activar entorno virtual
```
source myenv/bin/activate
```
El proyecto cuenta con un archivo requirements.txt donde se encuentran listadas todas las dependencias que requiere el proyecto para su correcta ejecución.
```
pip install -r requirements.txt
```

*Si se instalan nuevas dependencias es necesario mantener este archivo actualizado para ello se debe ejecutar:*
```
pip freeze > requirements.txt
```
Una vez instaladas todas las dependencias procedemos a cambiar la conexión a la base de datos por nuestra versión en local.
Para ello nos dirigimos a la ruta `./cabuto/settings.py`. Aquí buscaremos el siguiente bloque codigo:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CabutoShop$marketdb',
        'USER': 'CabutoShop',
        'PASSWORD': 'market2020',
        'HOST': 'CabutoShop.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }

    }
}
```
y lo reemplazamos por la conexión a nuestra base de datos en local, por ejemplo con postgresql:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CabutoShop',
        'USER': 'postgres',
        'PASSWORD': '124356*/',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
```
