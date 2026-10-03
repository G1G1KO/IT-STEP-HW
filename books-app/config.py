from os import urandom

class Config:
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_ECHO = True
    SECRET_KEY = urandom(32)