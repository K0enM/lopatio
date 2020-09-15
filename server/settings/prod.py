""" Production Settings """

import os
import dj_database_url
from .dev import *

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG=False

DATABASES = {
    'default': dj_database_url.config(
        default=environ('DATABASE_URL')
    )
}

ALLOWED_HOSTS = [os.getenv('DOMAIN')]