from apscheduler.schedulers.background import BackgroundScheduler

from HN.job2 import load_db


class MyClass:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def schedule(self):
        self.scheduler.add_job(self.myJob, 'interval', minutes=5)
        self.scheduler.start()

    def myJob(self):
        return load_db()

def start():
    my_scheduler = MyClass()
    my_scheduler.schedule()
