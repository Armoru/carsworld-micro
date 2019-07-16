import os


class Config(object):
    DEBUG = False
    DRF_HOST = 'djangoapp'
    DRF_PORT = 5000


class DevelopmentConfig(Config):
    DEBUG = True
    MEDIA_URL = f'http://localhost:{Config.DRF_PORT}'


class ProductionConfig(Config):
    DEBUG = False
    MEDIA_URL = "CHANGE TO DEPLOYED URL"
