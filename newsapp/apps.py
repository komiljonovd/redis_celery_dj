from django.apps import AppConfig


class NewsappConfig(AppConfig):
    name = 'newsapp'
    verbose_name = 'News'


    def ready(self):
        from . import signals