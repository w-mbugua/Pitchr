import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig:
    pass
class TestConfig:
    pass
class DevConfig:
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}