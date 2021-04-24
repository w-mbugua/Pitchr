import os

class Config:
    pass
    
class ProdConfig:
    pass

class TestConfig:
    pass

class DevConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}