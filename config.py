import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.getenv('DB_URI')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)