<<<<<<< HEAD
#from unipath import Path

"""
Django settngs for sigamosaprendiendo project.
=======
 

"""
Django settings for sigamosaprendiendo project.
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
<<<<<<< HEAD
#BASE_DIR =  Path(__file__).ancestor(3)
=======


>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(vlc7&p9@g&mwmu0^82n$cv%fa!z3k0$)xq@vpc%i0-%^=(pwi'

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
=======
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'south',
    'apps.home',
    'apps.inicio',

=======
    'apps.inicio',
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sigamosaprendiendo.urls'

WSGI_APPLICATION = 'sigamosaprendiendo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

<<<<<<< HEAD
LANGUAGE_CODE = 'es-mx'
=======
LANGUAGE_CODE = 'en-us'
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True 

STATIC_URL = '/static/'
<<<<<<< HEAD
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
TEMPLATE_DIRS = os.path.join(BASE_DIR,'templates')

#TEMPLATE_DIRS = [BASE_DIR.child('templates')]

#MEDIA_ROOT = RUTA_PROYECTO.child('media')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = 'http://localhost:8000/media/'
STATIC_ROOT = 'staticfiles'
 
# Configuracion del correo
#EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST = "smtp-mail.outlook.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sigamosaprendiendolaguna@outlook.com'
EMAIL_HOST_PASSWORD = '******'
EMAIL_USE_TLS = True
=======
TEMPLATE_DIRS = os.path.join(BASE_DIR,'templates')
>>>>>>> 2cf06878d7ea69d846cbf3821250260cce6c9faf
