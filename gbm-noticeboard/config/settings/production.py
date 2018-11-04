from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='')
DEBUG = env.bool('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = [env('DJANGO_ALLOWED_HOSTS')]