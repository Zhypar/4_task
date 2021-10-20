from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config('DEBUG', cast=bool)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/config('DB_NAME'),
    }
}