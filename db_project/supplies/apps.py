from django.apps import AppConfig


class SuppliesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'supplies'
    verbose_name = 'Поставки'
    
    def ready(self):
        import supplies.signals  # noqa