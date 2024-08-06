import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insy_cy++nif!cf)a=vo7*!=y4e=nb3b=3di0wy#5=dc^t5lgky$q'

DEBUG = False


ALLOWED_HOSTS = ["www.asv-led.by", "127.0.0.1", "93.125.99.54"]

DATABASES = {
                                # !!!ВЗЯТЬ НА ХОСТЕРЕ!!!
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'asv',
        'USER': 'sqlite',
        'PASSWORD': '5DdkI#2qr+2H',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
