import os
from settings import *

ALLOWED_HOSTS = "localhost"
SECRET_KEY = 'dfdjkhfdjshfj7676dfhgsdj'
DEBUG = "False"


DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'db.sqlite3',
         }
}
