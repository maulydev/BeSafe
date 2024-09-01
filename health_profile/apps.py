from django.apps import AppConfig


class HealthProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_profile'
    
    def ready(self):
        import health_profile.signals
