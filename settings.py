# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


ALLOWED_HOSTS = "localhost"
DEBUG = "False"
STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
    os.path.join(pyconzadir, 'bower_components'),
)

STATIC_ROOT = os.path.join(pyconzadir, 'statics')
TEMPLATE_DIRS = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATE_DIRS


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
        "items": [{"name": "about_pyconzim", "label": _("About PyConZim"),
            "url": "/about-pyconzim"},
            {"name": "django_girls_harare", "label": _("About Django Girls Harare"),
            "url": "/django-girls-harare"
            }]},
    {"name": "venue", "label": _("Venue"),
     "url": reverse_lazy("wafer_page", args=("venue",))},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         # {"name": "???", "label": _(u"» ??? ★"),
         # "url": reverse_lazy("wafer_sponsor", args=(???,))},
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
         ]},
    {"menu": "talks", "label": _("Talks"),
      "items": [
         {"name": "submit-a-talk", "label": _("Submit A Talk"),
          "url": "/submit-a-talk"},
         #{"name": "schedule-next-up", "label": _("Next up"),
           #Fixed day
           #"url": "/schedule/current/?day=2016-10-01&time=08:30"},
          #"url": reverse_lazy("wafer_current")},
          {"name": "accepted-talks", "label": _("Accepted Talks"),
           "url": reverse_lazy("wafer_users_talks")},
        ]},
    {"menu": "events", "label": _("News"),
     "items": []},
   # {"menu": "previous-pycons", "label": _("Past PyConZAs"),
   #  "items": [
   #      {"name": "pyconza2012", "label": _("PyConZA 2012"),
   #       "url": "http://2012.za.pycon.org/"},
   #      {"name": "pyconza2013", "label": _("PyConZA 2013"),
   #       "url": "http://2013.za.pycon.org/"},
   #      {"name": "pyconza2014", "label": _("PyConZA 2014"),
   #       "url": "http://2014.za.pycon.org/"},
   #      {"name": "pyconza2015", "label": _("PyConZA 2015"),
   #       "url": "http://2015.za.pycon.org/"},
   #      ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com"},
    {"name": "googleplus", "label": "Google+",
     "image": "/static/img/googleplus.png",
     "url": "https://groups.google.com/forum/#!forum/zimpy"},
    {"name": "facebook", "label": "Facebook",
     "image": "/static/img/facebook.png",
     "url": "https://www.facebook.com/"},
)


CRISPY_TEMPLATE_PACK = 'bootstrap3'
MARKITUP_FILTER = ('markdown.markdown', {
    'safe_mode': False,
    'extensions': [
        'outline',
        'attr_list',
        'attr_cols',
        'markdown.extensions.tables',
    ],
})
# Use HTTPS jquery URL so it's accessible on HTTPS pages (e.g. editing a talk)
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js'

WAFER_TALKS_OPEN =  True
