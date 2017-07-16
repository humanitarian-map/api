from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "HOST": "localhost",
        "PORT": 5432,
        "USERNAME": "jespino",
        "PASSWORD": "",
        "NAME": "humanitarianmap"
    }
}
