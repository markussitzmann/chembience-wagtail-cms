from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5t)0@43i_9u6(%n$=5+r6fb+o#3jq#ufi8+4d7xpmxi5qf2d6$'

ALLOWED_HOSTS = os.environ['APP_VIRTUAL_HOSTNAME'].split(",")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
