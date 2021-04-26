import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USER")
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/pitch'
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://wddhdhwybxtzit:fa4e4dde1b02e0f58b5480337a42e9121d9f60d2adcc8572109814f3b5dd1e13@ec2-107-22-83-3.compute-1.amazonaws.com:5432/dcv7cfig0g4306'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/pitch_test'

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/pitch'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}