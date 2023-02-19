import os

class Config:
    SECRET_KEY = '9c492c5f6e48c4680987b6f9fd8c5685'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
