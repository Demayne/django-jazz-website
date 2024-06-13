from django.apps import AppConfig

class PersonalConfig(AppConfig):
    """
    Configuration for the 'personal' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'
