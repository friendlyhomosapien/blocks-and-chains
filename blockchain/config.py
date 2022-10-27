import os

class BaseConfig:
    TESTING = True
    CELERY_TIMEZONE = os.environ.get("CELERY_TIMEZONE", "UTC")
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")     
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")    

config = BaseConfig()
