from django.apps import AppConfig

class MmorpgappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MMoRPGapp'

    def ready(self) -> None:
        from . import signals



    default_app_config = 'MMoRPGapp.apps.MyAppConfig'
    



