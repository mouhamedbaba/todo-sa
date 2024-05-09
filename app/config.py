import os
import secrets

class AppConfig:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or secrets.token_bytes(16)

