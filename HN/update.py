from apscheduler.schedulers.background import BackgroundScheduler

from HN.views import load_db, load_db_after

max_item_url = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"


class MyClass:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def schedule(self):
        self.myJob()  # run your job immediately here, then scheduler
        self.scheduler.add_job(self.myJob1, 'interval', minutes=5)
        self.scheduler.start()

    def myJob(self):
        return load_db(max_item_url)

    def myJob1(self):
        return load_db_after(max_item_url)


def start():
    my_scheduler = MyClass()
    my_scheduler.schedule()
