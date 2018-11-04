from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='(8bc!a7-c8acqgl50y48k%m5f2ye7*+nz065f!fq1l9c1^$3pt')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']