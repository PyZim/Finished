import os
from wafer.settings import *

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

ALLOWED_HOSTS = "localhost"
SECRET_KEY = 'dfdjkhfdjshfj7676dfhgsdj'
DEBUG = True

WAFER_CONFERENCE_NAME = "PyConZim"
WAFER_CONFERENCE_DOMAIN = "dzidzo"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'anntelebiz@gmail.com'
# EMAIL_HOST_PASSWORD = 'zgrwwmadzyizzknw'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pycon',
        'USER': 'hamu',
        'PASSWORD': 'Louis2353/?',
        'OPTIONS': {
            'autocommit': True,
         },
         'HOST': '',
         'PORT': '',
    }
}
