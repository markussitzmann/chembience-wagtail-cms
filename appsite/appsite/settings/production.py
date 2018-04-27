from .base import *

ALLOWED_HOSTS = os.environ['APP_VIRTUAL_HOSTNAME'].split(",")

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
