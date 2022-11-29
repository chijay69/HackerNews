import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
from django.utils.datetime_safe import datetime


# the managers
class JobManager(models.Manager):
    def get_queryset(self):
        return super(JobManager, self).get_queryset().filter(type='job')


class StoryManager(models.Manager):
    def get_queryset(self):
        return super(StoryManager, self).get_queryset().filter(type='story')


class CommentManager(models.Manager):
    def get_queryset(self):
        return super(CommentManager, self).get_queryset().filter(type='comment')


class PollManager(models.Manager):
    def get_queryset(self):
        return super(PollManager, self).get_queryset().filter(type='poll')


class POManager(models.Manager):
    def get_queryset(self):
        return super(POManager, self).get_queryset().filter(type='pollopt')


def default_thing():
    return []


class BaseModel(models.Model):
    STATUS_CHOICES = (
        ('job', 'Job'),
        ('story', 'Story'),
        ('comment', 'Comment'),
        ('poll', 'Poll'),
        ('pollopt', 'Pollopt'),
    )

    by = models.CharField(max_length=250, blank=True, default='', null=True)
    time = models.DateTimeField(blank=True, auto_now=datetime.now())
    dead = models.BooleanField(blank=True, null=True, default=False)
    deleted = models.BooleanField(blank=True, null=True, default=False)
    kids = ArrayField(models.IntegerField(), default=default_thing, blank=True, null=True)
    type = models.CharField(max_length=250, choices=STATUS_CHOICES, default='job', null=True)

    REQUIRED_FIELD = ['id', 'type']

    objects = models.Manager()  # The default manager.

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return f'item_type : {self.type}, by : {self.by}'


class JobModel(BaseModel):
    text = models.CharField(max_length=8192, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)

    objects = models.Manager()  # The default manager.
    # custom managers
    job = JobManager()


class StoryModel(BaseModel):
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField()  # the story score or vote count
    title = models.CharField(max_length=250, blank=True, default='', null=True)
    url = models.URLField(blank=True, null=True)

    objects = models.Manager()  # The default manager.
    # custom managers
    story = StoryManager()


class CommentModel(BaseModel):
    parent = models.IntegerField(blank=True)  # ID of the parent field
    text = models.CharField(max_length=8192, blank=True, null=True)

    objects = models.Manager()  # The default manager.
    # custom managers
    comment = CommentManager()


class PollModel(BaseModel):
    parts = ArrayField(models.IntegerField(), default=default_thing, blank=True, null=True)
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField()  # the story score or vote count
    title = models.CharField(max_length=250, blank=True, null=True)
    text = models.CharField(max_length=8192, blank=True, null=True)

    objects = models.Manager()  # The default manager.
    # custom managers
    poll = PollManager()


class PolloptModel(BaseModel):
    parent = models.IntegerField(blank=True, null=True)  # ID of the parent field
    score = models.IntegerField(blank=True, null=True)  # the story score or vote count

    objects = models.Manager()  # The default manager.
    # custom managers
    pollopt = POManager()
