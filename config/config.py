import os
import datetime
from dotenv import load_dotenv

load_dotenv()

class Config:
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    TESTING = False
    CSRF_ENABLED = True
