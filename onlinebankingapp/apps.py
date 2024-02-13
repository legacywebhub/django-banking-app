from django.apps import AppConfig


class OnlinebankingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlinebankingapp'

    def ready(self):
        import onlinebankingapp.signals
