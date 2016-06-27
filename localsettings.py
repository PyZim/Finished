import os
from wafer.settings import *

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

ALLOWED_HOSTS = "dzidzo.pythonanywhere.com"
SECRET_KEY = 'dfdjkhfdjshfj7676dfhgsdj'
DEBUG = "False"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dzidzo$pycon',
        'USER': 'dzidzo',
        'PASSWORD': 'pyconzim/?',
        'OPTIONS': {
            'autocommit': True,
         },
         'HOST': 'dzidzo.mysql.pythonanywhere-services.com',
         'PORT': '',
    }
}
