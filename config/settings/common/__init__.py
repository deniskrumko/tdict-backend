from .auth import *  # noqa
from .installed_apps import *  # noqa
from .logging import *  # noqa
from .middleware import *  # noqa
from .paths import *  # noqa
from .rest_framework import *  # noqa
from .static import *  # noqa
from .templates import *  # noqa

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
ALLOWED_HOSTS = ['*']
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
