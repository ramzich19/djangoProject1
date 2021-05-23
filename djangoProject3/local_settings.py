from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'j7f0yzi(eo9hgcs_ah=lczfy=-to%t+)c+mkwo&hir(k5m0&f7'


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'journal.elab@gmail.com'
EMAIL_HOST_PASSWORD = 'elabjournal'
EMAIL_PORT = 587

ALLOWED_HOSTS = ["127.0.0.1", 'elab-journal.com', '185.5.206.9']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
