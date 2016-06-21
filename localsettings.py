import os
from settings import *

ALLOWED_HOSTS = "localhost"
SECRET_KEY = 'dfdjkhfdjshfj7676dfhgsdj'
DEBUG = "False"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pycon',
        }
}
