from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# This is so we can just run celery and have our django settings ready to go,
# since it may not be within the booted app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetomelbourne.settings')

from django.conf import settings  # noqa

app = Celery('pttime',
             broker='amqp://',
             backend='amqp://')


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
