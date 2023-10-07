from dotenv import load_dotenv
import os

load_dotenv()

if os.environ.get("DJANGO_ENV") == "PRODUCTION":
    from .production_settings import *
else:
    from .local_settings import *
