
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'j7f0yzi(eo9hgcs_ah=lczfy=-to%t+)c+mkwo&hir(k5m0&f7'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", 'elab-journal.com', '185.5.206.9']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'journal',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
