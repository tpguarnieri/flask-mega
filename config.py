import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random_secret_key'