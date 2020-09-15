""" Production Settings """

import os
import dj_database_url
from .dev import *


DATABASES = {
    'default': dj_database_url.config(
        default=environ('DATABASE_URL')
    )
}

ALLOWED_HOSTS = [env('DOMAIN')]