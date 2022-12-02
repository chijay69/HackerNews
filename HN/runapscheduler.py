import os
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from django.core.management.base import BaseCommand
from apscheduler.triggers.cron import CronTrigger

from HN.job2 import load_db, load_db1


logger = logging.getLogger(__name__)


def myJob1(self):
    return load_db1()


def my_job():
    return load_db1()


class MyClass(BaseCommand):
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def schedule(self):
        self.scheduler.add_jobstore(DjangoJobStore(), 'mongorestore')
        register_events(self.scheduler)

        self.scheduler.add_job(my_job, 'interval', id="my_job", minutes=5, max_instances=1)
        logger.info("Added job 'myJob'.")
        logger.info("Starting scheduler...")
        self.scheduler.start()
        print('started job')





def start():
    my_scheduler = MyClass()
    my_scheduler.schedule()
