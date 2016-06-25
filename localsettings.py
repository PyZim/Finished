import os
from wafer.settings import *

ALLOWED_HOSTS = "localhost"
SECRET_KEY = 'dfdjkhfdjshfj7676dfhgsdj'
DEBUG = "False"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pycon',
        'USER': 'hamu',
        'PASSWORD': 'popo/?',
        'OPTIONS': {
            'autocommit': True,
         },
         'HOST': 'localhost',
         'PORT': '',
    }
}
