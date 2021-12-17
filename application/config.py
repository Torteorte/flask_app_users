import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ['SECRET_KEY']
DATABASE = os.path.join('application/instance/application.sqlite')
FLASK_ENV = 'development'
