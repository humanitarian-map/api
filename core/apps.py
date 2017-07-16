from django.apps import AppConfig
from .signals import connect_signals


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        connect_signals()
