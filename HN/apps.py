from django.apps import AppConfig


class HnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HN'

# used for running apscheduler
    def ready(self):
        from HN import runapscheduler
        runapscheduler.start()


