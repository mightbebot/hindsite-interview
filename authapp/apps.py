from django.apps import AppConfig
from django.core.signals import request_finished

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authapp'

class AuthappConfig(AppConfig):
    name = 'authapp'

    def ready(self):
        from . import signals
