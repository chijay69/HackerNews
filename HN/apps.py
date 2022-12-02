from django.apps import AppConfig


class HnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HN'

# used for running appscheduler
    def ready(self):
        # or use backgroundsheduler
        # from HN import update
        # update.start()
        # use django-apsheduler
        # from HN.runapscheduler import Command
        # Command().handle()


