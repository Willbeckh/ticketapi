from django.apps import AppConfig


class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickets'

    def ready(self):
        """override default ready method, to call background task when app starts"""
        from jobs import updater
        updater.start()