from django.apps import AppConfig


class CatalogAppConfig(AppConfig):
    name = "credentials.apps.catalog"
    verbose_name = "Catalog"

    def ready(self):
        import credentials.apps.catalog.eventing
