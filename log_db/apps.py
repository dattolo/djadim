from django.apps import AppConfig


class LogDbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'log_db'
    verbose_name = 'log'
