import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/pitch'

class ProdConfig:
    pass

class TestConfig:
    pass

class DevConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}