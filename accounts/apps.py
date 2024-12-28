from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

class YourAppConfig(AppConfig):
    name = 'internship_app'

    def ready(self):
        import accounts.signals  # Ensure the correct module path is used