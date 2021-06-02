"""
Development settings to override production settings.
"""
from environs import Env

env = Env()
env.read_env()


SECRET_KEY = env.str('DEV_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
