import time

from django.apps import AppConfig

new_stories_url = '/v0/newstories.json?print=pretty'


class HnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HN'

    def ready(self):
        from HN import update
        update.start()
